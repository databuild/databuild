from databuild.functional import guess_type
from databuild.operator import Operator
from .importer import Importer
from .exporter import BaseSheetExporter


class BaseWorkBook(object):
    sheet_class = None

    def __init__(self, name='workbook'):
        self.name = name
        self.sheets = {}
        self.operator = Operator(self)
        self.importer = Importer(self)
        super(BaseWorkBook, self).__init__()

    def __getitem__(self, key):
        return self.sheets[key]

    def add_sheet(self, name, headers):
        assert self.sheet_class is not None
        sheet = self.sheet_class(workbook=self, name=name, headers=headers)
        self.sheets[name] = sheet
        return sheet

    def import_data(self, format='csv', *args, **kwargs):
        return self.importer.import_data(format, *args, **kwargs)

    def apply_operations(self, build_file, echo=False):
        return self.operator.apply_operations(build_file, echo)

    def apply_operation(self, operation, echo=False):
        return self.operator.apply_operation(operation, echo)


class BaseWorkSheet(object):
    exporter_class = BaseSheetExporter

    def __init__(self, workbook, name, headers):
        self.workbook = workbook
        self.name = name
        self.headers = headers
        self.exporter = self.exporter_class(self)
        super(BaseWorkSheet, self).__init__()

    def guess_column_types(self, sample_size=5):
        headers = self.headers[:]
        for column in headers:
            values = self.get_column(column)[:sample_size]
            value_type = guess_type(values)
            transform = lambda x: value_type(x[column])
            self.update_column(column, transform)

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

    def export_data(self, format='csv'):
        return self.exporter.export_data(format)

    def print_data(self):
        raise NotImplementedError()
