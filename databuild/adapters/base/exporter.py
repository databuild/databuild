class BaseSheetExporter(object):
    def __init__(self, sheet):
        self.sheet = sheet
        super(BaseSheetExporter, self).__init__()

    def export_data(self, format='csv'):
        export_method = getattr(self, 'export_%s' % format, False)
        if export_method:
            return export_method()
        raise NotImplementedError()
