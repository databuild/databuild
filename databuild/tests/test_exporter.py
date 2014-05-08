import json
import os
from tablib.formats._yaml import yaml
from unittest import TestCase

from databuild.adapters.locmem.models import LocMemBook
from databuild.adapters.base import importer


TEST_DIR = os.path.join(os.path.dirname(__file__))

class ExporterTestCase(TestCase):
    def setUp(self):
        self.book = LocMemBook('project1')
        self.dataimporter = importer.Importer(workbook=self.book)
        self.sheet = self.dataimporter.import_data('csv', os.path.join(TEST_DIR, "dataset1.csv"), 'sheet1', guess_types=False)

    def test_json(self):
        data = self.sheet.export_data(format='json')
        parsed = json.loads(data)
        assert len(parsed) == 191

    def test_headers(self):
        data = self.sheet.export_data(format='json', headers=["Totale Maschi", "Totale Fammine"])
        parsed = json.loads(data)
        assert len(parsed) == 191
        assert len(parsed[0].keys()) == 2
        assert self.book.sheets.keys() == [self.sheet.name]

    def test_yml(self):
        data = self.sheet.export_data(format='yaml')
        parsed = yaml.load(data)
        assert len(parsed) == 191

    def test_xls(self):
        self.sheet.export_data(format='xls')
        # I have no idea how to test this

    def test_csv(self):
        data = self.sheet.export_data(format='csv')
        assert len(data.splitlines()) == 192

