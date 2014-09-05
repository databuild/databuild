try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO
import six
import json
import os

if six.PY2:
    from databuild.vendor import unicodecsv as csv
else:
    import csv

from databuild.compat import _open


class Importer(object):
    def __init__(self, workbook, relative_path):
        self.workbook = workbook
        self.relative_path = relative_path
        super(Importer, self).__init__()

    def import_data(self, format, filename, sheet_name=None, *args, **kwargs):
        if sheet_name is None:
            sheet_name = os.path.basename(filename)

        if not os.path.exists(filename) and self.relative_path:
            filename = os.path.join(self.relative_path, filename)

        import_method = getattr(self, 'import_%s' % format, False)
        if import_method:
            return import_method(filename, sheet_name, *args, **kwargs)
        raise NotImplementedError()

    def import_csv(self, filename, sheet_name, headers=None, encoding='utf-8', skip_first_lines=0, skip_last_lines=0, guess_types=True, **kwargs):
        with _open(filename, 'r', encoding=encoding) as f:
            if skip_last_lines:
                lines = f.readlines()[skip_first_lines:-skip_last_lines]
            else:
                lines = f.readlines()[skip_first_lines:]
        _buffer = StringIO('\n'.join(lines))
        _buffer.seek(0)

        reader = csv.DictReader(_buffer, **kwargs)
        if headers is None:
            headers = reader.fieldnames

        sheet = self.workbook.add_sheet(sheet_name, headers)
        sheet.extend(reader)

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
