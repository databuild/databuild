import os
import six
from unittest import TestCase

from databuild.adapters.locmem.models import LocMemBook
from databuild.adapters.base.exceptions import DoesNotExist
from databuild.adapters.base import importer


TEST_DIR = os.path.join(os.path.dirname(__file__))

class ImporterTestCase(TestCase):
    def test_unicode_csv_dict_reader(self):
        filename = os.path.join(TEST_DIR, "dataset1.csv")

        with open(filename, 'rb') as f:
            reader = importer.UnicodeDictReader(f, 'utf-8')
            row = list(reader)[0]

        assert isinstance(row, dict)
        assert isinstance(list(row.keys())[0], six.text_type)
        assert isinstance(list(row.values())[0], six.text_type)

    def test_import_csv(self):
        book = LocMemBook('project1')
        dataimporter = importer.Importer(workbook=book)
        sheet = dataimporter.import_data('csv', os.path.join(TEST_DIR, "dataset1.csv"), 'sheet1', guess_types=False)

        acqui_test = {
            "Codice Comune": '6001',
            "Comune": "Acqui Terme",
            "Totale Maschi": '9510',
            "Totale Femmine": '10939',
            "Maschi+Femmine": '20449'
        }

        acqui = sheet.get(Comune="Acqui Terme")
        assert acqui == acqui_test

        short_sheet = dataimporter.import_data('csv', os.path.join(TEST_DIR, "dataset1.csv"), 'sheet2', skip_first_lines=2, guess_types=False)

        self.assertRaises(DoesNotExist, short_sheet.get, Comune="Acqui Terme")
        short_sheet.get(Comune="Voltaggio")
        assert len(short_sheet.all()) == len(sheet.all()) - 2

        short_sheet2 = dataimporter.import_data('csv', os.path.join(TEST_DIR, "dataset1.csv"), 'sheet3', skip_last_lines=2, guess_types=False)

        self.assertRaises(DoesNotExist, short_sheet2.get, Comune="Voltaggio")
        assert len(short_sheet2.all()) == len(sheet.all()) - 2

        guessed_sheet = dataimporter.import_data('csv', os.path.join(TEST_DIR, "dataset1.csv"), 'sheet4', skip_last_lines=1)

        acqui_test = {
            "Codice Comune": 6001,
            "Comune": "Acqui Terme",
            "Totale Maschi": 9510,
            "Totale Femmine": 10939,
            "Maschi+Femmine": 20449
        }

        acqui = guessed_sheet.get(Comune="Acqui Terme")
        assert acqui == acqui_test

    def test_import_json(self):
        book = LocMemBook('project1')
        dataimporter = importer.Importer(workbook=book)
        sheet = dataimporter.import_data('json', os.path.join(TEST_DIR, "dataset1.json"), 'sheet1')
        acqui_test = {
            "Codice Comune": '6001',
            "Comune": "Acqui Terme",
            "Totale Maschi": '9510',
            "Totale Femmine": '10939',
            "Maschi+Femmine": '20449'
        }

        acqui = sheet.get(Comune="Acqui Terme")
        assert acqui == acqui_test
