from ..base.exporter import BaseSheetExporter

class SheetExporter(BaseSheetExporter):
    def export_csv(self, *args, **kwargs):
        return self.sheet.data.csv

    def export_json(self, *args, **kwargs):
        return self.sheet.data.json

    def export_yaml(self, *args, **kwargs):
        return self.sheet.data.yaml

    def export_xls(self, *args, **kwargs):
        return self.sheet.data.xls
