class SheetExporter(object):
    def __init__(self, sheet):
        self.sheet = sheet
        super(SheetExporter, self).__init__()

    def export_data(self, format='csv'):
        export_method = getattr(self, 'export_%s' % format, False)
        if export_method:
            return export_method()
        raise NotImplementedError()

    def export_csv(self):
        return self.sheet.data.csv

    def export_json(self):
        return self.sheet.data.json

    def export_yaml(self):
        return self.sheet.data.yaml

    def export_xls(self):
        return self.sheet.data.xls
