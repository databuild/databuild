import os
import shelve
from tempfile import gettempdir

from ..locmem.models import LocMemBook, LocMemSheet


class ShelveSheet(LocMemSheet):
    headers = tuple()

    def sync(self):
        self.workbook.sync(self)

    def update_column(self, *args, **kwargs):
        _super = super(ShelveSheet, self).update_column(*args, **kwargs)
        self.sync()
        return _super

    def append_column(self, *args, **kwargs):
        _super = super(ShelveSheet, self).append_column(*args, **kwargs)
        self.sync()
        return _super

    def remove_column(self, *args, **kwargs):
        _super = super(ShelveSheet, self).remove_column(*args, **kwargs)
        self.sync()
        return _super

    def copy_column(self, *args, **kwargs):
        _super = super(ShelveSheet, self).copy_column(*args, **kwargs)
        self.sync()
        return _super

    def rename_column(self, *args, **kwargs):
        _super = super(ShelveSheet, self).rename_column(*args, **kwargs)
        self.sync()
        return _super

    def append(self, *args, **kwargs):
        _super = super(ShelveSheet, self).append(*args, **kwargs)
        self.sync()
        return _super

    def pop_rows(self, *args, **kwargs):
        _super = super(ShelveSheet, self).pop_rows(*args, **kwargs)
        self.sync()
        return _super

    def extend(self, *args, **kwargs):
        _super = super(ShelveSheet, self).extend(*args, **kwargs)
        self.sync()
        return _super

    def update_rows(self, *args, **kwargs):
        _super = super(ShelveSheet, self).update_rows(*args, **kwargs)
        self.sync()
        return _super

    def delete(self, *args, **kwargs):
        _super = super(ShelveSheet, self).delete(*args, **kwargs)
        self.sync()
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

    def __del__(self):
        self.sync()
        self.data.close()
        super(ShelveBook, self).__del__()

    def sync(self, sheet=None):
        if sheet:
            self.data[sheet.name] = sheet.serialize()
        else:
            for name, sheet in self.sheets.items():
                self.data[name] = sheet.serialize()
        self.data.sync()

    def add_sheet(self, *args, **kwargs):
        return super(ShelveBook, self).add_sheet(*args, **kwargs)
        self.sync()

    def remove_sheet(self, *args, **kwargs):
        return super(ShelveBook, self).remove_sheet(*args, **kwargs)
        self.sync()


