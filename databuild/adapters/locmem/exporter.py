from ..base.exporter import BaseSheetExporter

class SheetExporter(BaseSheetExporter):
    def export_csv(self):
        return self.sheet.data.csv

    def export_json(self):
        return self.sheet.data.json

    def export_yaml(self):
        return self.sheet.data.yaml

    def export_xls(self):
        return self.sheet.data.xls
