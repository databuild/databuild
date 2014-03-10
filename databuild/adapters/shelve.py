import os
from tempfile import gettempdir

from .base import BaseWorkBook, BaseWorkSheet
from .exceptions import DoesNotExist
import offtheshelf


class ShelveSheet(BaseWorkSheet):
    headers = tuple()

    def __init__(self, workbook, name, headers):
        self.db = workbook.db
        super(ShelveSheet, self).__init__(workbook, name, headers)

    def update_column(self, column_name, callable_or_values, filter_fn=None):
        with offtheshelf.openDB(self.db) as db:
            collection = db.get_collection(self.name)
            if filter_fn is None:
                rows = collection.find()
            else:
                rows = [d for d in collection.find() if filter_fn(d)]
            for i, row in enumerate(rows):
                if callable(callable_or_values):
                    value = callable_or_values(row)
                else:
                    value = callable_or_values[i]
                row[column_name] = value

    def append_column(self, column_name, callable_or_values=None):
        if callable_or_values is None:
            callable_or_values = lambda x: None
        self.headers.append(column_name)
        self.update_column(column_name, callable_or_values)

    def remove_column(self, column_name):
        self.headers.remove(column_name)
        with offtheshelf.openDB(self.db) as db:
            collection = db.get_collection(self.name)
            for row in collection:
                del row[column_name]

    def copy_column(self, old_name, new_name):
        self.headers.append(new_name)
        with offtheshelf.openDB(self.db) as db:
            collection = db.get_collection(self.name)
            for row in collection:
                row[new_name] = row[old_name]

    def rename_column(self, old_name, new_name):
        self.headers.append(new_name)
        self.headers.remove(old_name)
        with offtheshelf.openDB(self.db) as db:
            collection = db.get_collection(self.name)
            for row in collection:
                row[new_name] = row[old_name]
                del row[old_name]

    def get_column(self, column_name):
        with offtheshelf.openDB(self.db) as db:
            collection = db.get_collection(self.name)
            values = [row[column_name] for row in collection]
        return values

    def all(self):
        with offtheshelf.openDB(self.db) as db:
            collection = db.get_collection(self.name)
            results = [d for d in collection.find()]
        return results

    def filter(self, fn):
        with offtheshelf.openDB(self.db) as db:
            collection = db.get_collection(self.name)
            results = [d for d in collection.find() if fn(d)]
        return results

    def get(self, **lookup):
        with offtheshelf.openDB(self.db) as db:
            collection = db.get_collection(self.name)
            result = collection.find_one(lookup)
        if result is None:
            raise DoesNotExist()
        return result

    def append(self, doc):
        doc = dict([(header, doc.get(header, None)) for header in self.headers])
        with offtheshelf.openDB(self.db) as db:
            collection = db.get_collection(self.name)
            collection.insert(doc)

    def extend(self, docs):
        with offtheshelf.openDB(self.db) as db:
            for doc in docs:
                doc = dict([(header, doc.get(header, None)) for header in self.headers])
                collection = db.get_collection(self.name)
                collection.insert(doc)

    def update_rows(self, fn, callable_or_doc):
        with offtheshelf.openDB(self.db) as db:
            collection = db.get_collection(self.name)
            results = [d for d in collection.find() if fn(d)]
            for result in results:
                if callable(callable_or_doc):
                    update = callable_or_doc(result)
                else:
                    update = callable_or_doc
                result.update(update)

    def delete(self, fn):
        with offtheshelf.openDB(self.db) as db:
            collection = db.get_collection(self.name)
            collection._docs = [d for d in collection.find() if not fn(d)]


class ShelveBook(BaseWorkBook):
    sheet_class = ShelveSheet

    def __init__(self, name='workbook', data_dir=None):
        # TODO: slugify name
        if not data_dir:
            data_dir = gettempdir()
        self.db = os.path.join(data_dir, name)
        super(ShelveBook, self).__init__(name)
