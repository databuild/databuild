from __future__ import absolute_import
import errno
import os
import socket
import time
from tempfile import gettempdir

from .locmem import LocMemBook, LocMemSheet
import shelve


class ShelveSheet(LocMemSheet):
    headers = tuple()

    def update_column(self, *args, **kwargs):
        _super = super(ShelveSheet, self).update_column(*args, **kwargs)
        self.workbook.sync()
        return _super

    def append_column(self, *args, **kwargs):
        _super = super(ShelveSheet, self).append_column(*args, **kwargs)
        self.workbook.sync()
        return _super

    def remove_column(self, *args, **kwargs):
        _super = super(ShelveSheet, self).remove_column(*args, **kwargs)
        self.workbook.sync()
        return _super

    def copy_column(self, *args, **kwargs):
        _super = super(ShelveSheet, self).copy_column(*args, **kwargs)
        self.workbook.sync()
        return _super

    def rename_column(self, *args, **kwargs):
        _super = super(ShelveSheet, self).rename_column(*args, **kwargs)
        self.workbook.sync()
        return _super

    def get_column(self, *args, **kwargs):
        return super(ShelveSheet, self).get_column(*args, **kwargs)

    def all(self, *args, **kwargs):
        return super(ShelveSheet, self).all(*args, **kwargs)

    def filter(self, *args, **kwargs):
        return super(ShelveSheet, self).filter(*args, **kwargs)

    def get(self, *args, **kwargs):
        return super(ShelveSheet, self).get(*args, **kwargs)

    def append(self, *args, **kwargs):
        _super = super(ShelveSheet, self).append(*args, **kwargs)
        self.workbook.sync()
        return _super

    def extend(self, *args, **kwargs):
        _super = super(ShelveSheet, self).extend(*args, **kwargs)
        self.workbook.sync()
        return _super

    def update_rows(self, *args, **kwargs):
        _super = super(ShelveSheet, self).update_rows(*args, **kwargs)
        self.workbook.sync()
        return _super

    def delete(self, *args, **kwargs):
        _super = super(ShelveSheet, self).delete(*args, **kwargs)
        self.workbook.sync()
        return _super

    def serialize(self):
        return {
            'headers': self.headers,
            'data': self.data
        }


class ShelveBook(LocMemBook):
    sheet_class = ShelveSheet

    def __init__(self, name='workbook', data_dir=None):
        super(ShelveBook, self).__init__(name)
        # TODO: slugify name
        if not data_dir:
            data_dir = gettempdir()
        self.db = os.path.join(data_dir, name)
        self.data = shelve.open(self.db)

    def sync(self):
        for name, sheet in self.sheets.items():
            self.data[name] = sheet.serialize()
        self.data.sync()

    def __del__(self):
        self.sync()
        self.data.close()
        super(ShelveBook, self).__del__()


