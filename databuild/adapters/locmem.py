from .base import BaseWorkBook, BaseWorkSheet
from .exceptions import DoesNotExist
import tablib
from tabulate import tabulate
from collections import OrderedDict
try:
    from databuild.formats import _pyaml
except ImportError:
    _pyaml = False

class LocMemSheet(BaseWorkSheet):
    def __init__(self, workbook, name, headers):
        if _pyaml:
            formats = list(tablib.formats.available)
            formats.append(_pyaml) 
            tablib.formats.available = formats
            tablib.Dataset.pyml = property()

        self.data = tablib.Dataset(headers=headers)
        super(LocMemSheet, self).__init__(workbook, name, headers)

    def __getitem__(self, key):
        return self._values_to_dict(self.data[key])

    def _match(self, doc, where):
        """Return True if 'doc' matches the 'where' condition."""
        assert isinstance(where, dict), "where is not a dictionary"
        assert isinstance(doc, dict), "doc is not a dictionary"
        try:
            return all([doc[k] == v for k, v in where.items()])
        except KeyError:
            return False

    def _lookup_to_fn(self, lookup):
        return lambda r: self._match(r, lookup)

    def _values_to_dict(self, values):
        return OrderedDict(zip(self.data.headers, values))

    def _dict_to_values(self, doc):
        if isinstance(doc, OrderedDict):
            return tuple(doc.values())
        return [doc[k] for k in self.data.headers if k in doc]

    def _callable_or_docs(self, callable_or_docs, items=None):
        if callable(callable_or_docs):
            assert items != None
            return [callable_or_docs(item) for item in items]
        return callable_or_docs

    def get_sheet(self, sheet):
        return self.sheets[sheet]

    def append_column(self, column_name, callable_or_values=None):
        if callable_or_values is None:
            callable_or_values = lambda x: None
        values = self._callable_or_docs(callable_or_values, self.data.dict)
        self.headers.append(column_name)
        self.data.append_col(values, header=column_name)

    def copy_column(self, old_name, new_name):
        values = self.data[old_name]
        self.append_column(new_name, values)

    def remove_column(self, column_name):
        del self.data[column_name]
        self.headers.remove(column_name)

    def rename_column(self, old_name, new_name):
        self.copy_column(old_name, new_name)
        self.remove_column(old_name)

    def update_column(self, column_name, callable_or_values, filter_fn=None):
        if filter_fn is None:
            tmp_name = "__%s__" % column_name
            self.append_column(tmp_name, callable_or_values)
            self.remove_column(column_name)
            self.rename_column(tmp_name, column_name)
        else:
            def fn(r):
                r[column_name] = callable_or_values(r)
                return r
            self.update_rows(filter_fn, fn)

    def get_column(self, column_name):
        return self.data[column_name]

    def all(self):
        return self.data.dict

    def filter(self, fn):
        return [d for d in self.data.dict if fn(d)]

    def get(self, **lookup):
        try:
            fn = self._lookup_to_fn(lookup)
            return self.filter(fn)[0]
        except IndexError:
            raise DoesNotExist()

    def append(self, doc):
        for header in self.data.headers:
            if header not in doc:
                doc[header] = None
        self.data.append(self._dict_to_values(doc))

    def pop_rows(self, rows_count):
        for i in range(rows_count):
            self.data.pop()

    def extend(self, docs):
        [self.append(doc) for doc in docs]

    def update_rows(self, fn, callable_or_doc):
        results = self.filter(fn)
        docs = results[:]
        for doc in docs:
            if callable(callable_or_doc):
                update = callable_or_doc(doc)
            else:
                update = callable_or_doc
            doc.update(update)
        self.delete(fn)

        rows = [self._dict_to_values(doc) for doc in docs]
        [self.data.append(r) for r in rows]

    def delete(self, fn):
        docs = [self._dict_to_values(doc) for doc in self.data.dict if not fn(doc) ]
        self.data = tablib.Dataset(*docs, headers=self.data.headers)

    def print_data(self):
        print(tabulate(self.data, headers=self.headers))

    def export_data(self, format='csv'):
        export_method = getattr(self, 'export_%s' % format, False)
        if export_method:
            return export_method()
        raise NotImplementedError()

    def export_csv(self):
        return self.data.csv

    def export_json(self):
        return self.data.json

    def export_yaml(self):
        if _pyaml:
            return self.data.pyaml
        return self.data.yaml

    def export_xls(self):
        return self.data.xls


class LocMemBook(BaseWorkBook):
    sheet_class = LocMemSheet
