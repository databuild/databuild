class BaseSheetExporter(object):
    def __init__(self, sheet):
        self.sheet = sheet
        super(BaseSheetExporter, self).__init__()

    def export_data(self, format='csv', headers=None, *args, **kwargs):
        if headers:
            sheet = self.sheet.copy(dest="__tmp__", headers=headers)
        else:
            sheet = self.sheet
        export_method = getattr(sheet.exporter, 'export_%s' % format, False)
        if export_method:
            data = export_method(*args, **kwargs)
            if headers:
                sheet.destroy()
            return data
        raise NotImplementedError()
