from databuild.functional import guess_type
from databuild.operator import Operator
from .importer import Importer
from .exporter import BaseSheetExporter

from databuild import settings as default_settings


class BaseWorkBook(object):
    sheet_class = None
    importer_class = Importer

    def __init__(self, name='workbook', settings=None):
        if settings is None:
            settings = default_settings
        self.settings = settings

        self.name = name
        self.sheets = {}
        self.operator = Operator(self, settings=settings)
        super(BaseWorkBook, self).__init__()

    def __getitem__(self, key):
        return self.sheets[key]

    def add_sheet(self, name, headers):
        assert self.sheet_class is not None
        sheet = self.sheet_class(workbook=self, name=name, headers=headers)
        self.sheets[name] = sheet
        return sheet

    def remove_sheet(self, sheet):
        self.sheets.pop(sheet.name)

    def import_data(self, filename, relative_path=None, format='csv', *args, **kwargs):
        importer = self.importer_class(self, relative_path=relative_path)
        return importer.import_data(format, filename, *args, **kwargs)

    def apply_operations(self, build_files, echo=False):
        return self.operator.apply_operations(build_files, echo)

    def apply_operation(self, operation, build_file=None, echo=False):
        return self.operator.apply_operation(operation, build_file, echo)


class BaseWorkSheet(object):
    exporter_class = BaseSheetExporter

    def __init__(self, workbook, name, headers):
        self.workbook = workbook
        self.name = name
        self.headers = headers
        self.exporter = self.exporter_class(self)
        super(BaseWorkSheet, self).__init__()

    def __getitem__(self, key):
        """
        Returns the nth
        """
        raise NotImplementedError

    def __len__(self):
        """
        Returns the row count
        """
        raise NotImplementedError

    def guess_column_types(self, sample_size=5):
        headers = self.headers[:]
        for column in headers:
            values = self.get_column(column)[:sample_size]
            value_type = guess_type(values)
            transform = lambda x: value_type(x[column])
            self.update_column(column, transform)


    def copy(self, dest, headers=None):
        src_headers = self.headers
        filter_columns = False

        if headers is None:
            headers = src_headers
        else:
            filter_columns = True
            excluded_headers = set(src_headers) - set(headers)

        dest_sheet = self.workbook.add_sheet(name=dest, headers=headers)

        if not filter_columns:
            dest_sheet.extend(self.all())
        else:
            for src_doc in self.all():
                dest_doc = src_doc.copy()
                [dest_doc.pop(k) for k in excluded_headers]
                dest_sheet.append(dest_doc)
        return dest_sheet

    def destroy(self):
        self.workbook.remove_sheet(self)

    def append_column(self, column_name, callable_or_values=None):
        raise NotImplementedError()

    def remove_column(self, column_name):
        raise NotImplementedError()

    def rename_column(self, old_name, new_name):
        raise NotImplementedError()

    def copy_column(self, old_name, new_name):
        raise NotImplementedError()

    def update_column(self, column_name, callable_or_values, filter_fn=None):
        raise NotImplementedError()

    def get_column(self, column_name):
        raise NotImplementedError()

    def get(self, **lookup):
        raise NotImplementedError()

    def all(self):
        raise NotImplementedError()
        
    def filter(self,  fn):
        raise NotImplementedError()

    def append(self, doc):
        raise NotImplementedError()

    def pop_rows(self, rows_count):
        raise NotImplementedError()

    def extend(self, docs):
        raise NotImplementedError()

    def update_rows(self, fn, callable_or_doc):
        raise NotImplementedError()

    def delete(self, fn):
        raise NotImplementedError()

    def apply_operation(self, operation):
        assert operation['params']['sheet'] == self.name
        return self.workbook.apply_operation(operation)

    def export_data(self, format='csv', headers=None, *args, **kwargs):
        return self.exporter.export_data(format=format, headers=headers, *args, **kwargs)

    def print_data(self):
        raise NotImplementedError()
