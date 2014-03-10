import os
import six
from unittest import TestCase

from databuild.adapters.locmem import LocMemBook
from databuild import importer


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
        sheet = dataimporter.import_data('csv', os.path.join(TEST_DIR, "dataset1.csv"), 'sheet1')

        acqui_test = {
            "Codice Comune": '6001',
            "Comune": "Acqui Terme",
            "Totale Maschi": '9510',
            "Totale Femmine": '10939',
            "Maschi+Femmine": '20449'
        }

        acqui = sheet.get(Comune="Acqui Terme")
        assert acqui == acqui_test
