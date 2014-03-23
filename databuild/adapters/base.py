from databuild.operator import Operator
from databuild.importer import Importer


class BaseWorkBook(object):
    sheet_class = None

    def __init__(self, name='workbook'):
        self.name = name
        self.sheets = {}
        self.operator = Operator(self)
        self.importer = Importer(self)
        super(BaseWorkBook, self).__init__()

    def add_sheet(self, name, headers):
        assert self.sheet_class is not None
        sheet = self.sheet_class(workbook=self, name=name, headers=headers)
        self.sheets[name] = sheet
        return sheet

    def import_data(self, format='csv', *args, **kwargs):
        return self.importer.import_data(format, *args, **kwargs)

    def apply_operations(self, operations, echo=False):
        [self.apply_operation(op, echo) for op in operations]

    def apply_operation(self, operation, echo=False):
        return self.operator.apply_operation(operation, echo)


class BaseWorkSheet(object):
    def __init__(self, workbook, name, headers):
        self.workbook = workbook
        self.name = name
        self.headers = headers
        super(BaseWorkSheet, self).__init__()

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
        raise NotImplementedError()

    def print_data(self):
        raise NotImplementedError()
