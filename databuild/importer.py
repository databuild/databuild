import six
import json
import os, csv, codecs


class UTF8Recoder(object):
    """
    Iterator that reads an encoded stream and reencodes the input to UTF-8
    """
    def __init__(self, f, encoding):
        self.reader = codecs.getreader(encoding)(f)
        super(UTF8Recoder, self).__init__()

    def __iter__(self):
        return self

    def next(self):
        return self.reader.next().encode("utf-8")

    def __next__(self):
        # used by Py3k
        return self.reader.__next__()


class UnicodeDictReader(object):
    """
    A CSV reader which will iterate over lines in the CSV file "f",
    which is encoded in the given encoding.
    """

    def __init__(self, f, encoding="utf-8", **kwargs):
        super(UnicodeDictReader, self).__init__()
        f = UTF8Recoder(f, encoding)
        self.reader = csv.DictReader(f, **kwargs)

    def next(self):
        row = self.reader.next()
        return {six.text_type(k, "utf-8"): six.text_type(v, "utf-8") for k, v in row.items()}

    def __iter__(self):
        return self

    def __next__(self):
        # used by Py3k
        row = self.reader.__next__()
        return {six.text_type(k): six.text_type(v) for k, v in row.items()}

    def __getattr__(self, name):
        if hasattr(self.reader, name):
            return getattr(self.reader, name)
        raise AttributeError()

if six.PY2:
    def _open(*args, **kwargs):
        kwargs.pop('encoding', False)
        return open(*args, **kwargs) 
else:
    _open = open


class Importer(object):
    def __init__(self, workbook):
        self.workbook = workbook
        super(Importer, self).__init__()

    def import_data(self, format, filename, sheet_name=None, *args, **kwargs):
        if sheet_name is None:
            sheet_name = os.path.basename(filename)

        import_method = getattr(self, 'import_%s' % format, False)
        if import_method:
            return import_method(filename, sheet_name, *args, **kwargs)
        raise NotImplementedError()

    def import_csv(self, filename, sheet_name, headers=None, encoding='utf-8', **kwargs):
        with open(filename, 'rb') as f:
            reader = UnicodeDictReader(f, encoding, **kwargs)
            if headers is None:
                headers = reader.fieldnames

            sheet = self.workbook.add_sheet(sheet_name, headers)
            sheet.extend(reader)
        return sheet

    def import_json(self, filename, sheet_name, headers=None, encoding='utf-8', **kwargs):
        with _open(filename, 'r', encoding=encoding) as fh:
            data = json.load(fh)
            if headers is None:
                headers = data[0].keys()

            sheet = self.workbook.add_sheet(sheet_name, headers)
            sheet.extend(data)
        return sheet
