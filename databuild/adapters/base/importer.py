import six
import json
import os

if six.PY2:
    import unicodecsv as csv
else:
    import csv

from databuild.compat import _open


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

    def import_csv(self, filename, sheet_name, headers=None, encoding='utf-8', skip_first_lines=0, skip_last_lines=0, guess_types=True, **kwargs):
        if not os.path.exists(filename):
            filename = os.path.join(os.path.dirname(self.workbook.operator.build_file), filename)

        with open(filename, 'rU') as f:
            reader = csv.DictReader(f, **kwargs)
            if headers is None:
                headers = reader.fieldnames

            sheet = self.workbook.add_sheet(sheet_name, headers)

            [next(reader) for i in range(skip_first_lines)]
            sheet.extend(reader)
            sheet.pop_rows(skip_last_lines)

        if guess_types:
            sheet.guess_column_types()
        return sheet

    def import_json(self, filename, sheet_name, headers=None, encoding='utf-8', **kwargs):
        with _open(filename, 'r', encoding=encoding) as fh:
            data = json.load(fh)
            if headers is None:
                headers = data[0].keys()

            sheet = self.workbook.add_sheet(sheet_name, headers)
            sheet.extend(data)
        return sheet
