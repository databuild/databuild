import os
from unittest import TestCase

from databuild.adapters import shelve2 as shelve
from databuild.adapters import locmem
from databuild.adapters import exceptions


TEST_DIR = os.path.join(os.path.dirname(__file__))

class BaseAdapterMixin(object):
    workbook_class = None

    def setup_book(self):
        return self.workbook_class(name='test_workbook')

    def setUp(self):
        self.book = self.setup_book()
        self.sheet = self.book.add_sheet('students', ["Codice Comune", "Comune", "Totale Maschi", "Totale Femmine"])

        self.acqui = {
            "Codice Comune": 6001,
            "Comune": "Acqui Terme",
            "Totale Maschi": 9510,
            "Totale Femmine": 10939
        }
        self.sheet.append(self.acqui)
        row = {
            "Codice Comune": 6002,
            "Comune": "Albera Ligure",
            "Totale Maschi": 181,
            "Totale Femmine": 157
        }
        self.sheet.append(row)
        row = {
            "Codice Comune": 6003,
            "Comune": "Alessandria",
            "Totale Maschi": 44897,
            "Totale Femmine": 49294
        }
        self.sheet.append(row)

    def test_adapter_get(self):
        fetched_row = self.sheet.get(Comune="Acqui Terme")
        assert fetched_row == self.acqui

        fetched_row = self.sheet.get(**{"Totale Femmine": 10939})
        assert fetched_row["Comune"] == "Acqui Terme"

    def test_adapter_delete_row(self):
        self.sheet.delete(lambda r: r['Comune'] == "Acqui Terme")
        self.assertRaises(exceptions.DoesNotExist, self.sheet.get, Comune="Acqui Terme")

    def test_adapter_copy_column(self):
        self.sheet.copy_column("Codice Comune", "Postal Code")
        assert "Codice Comune" in self.sheet.headers
        assert "Postal Code" in self.sheet.headers

        fetched_row = self.sheet.get(Comune="Acqui Terme")
        assert fetched_row['Codice Comune'] == fetched_row['Postal Code']

    def test_adapter_remove_column(self):
        self.sheet.remove_column("Codice Comune")
        assert "Codice Comune" not in self.sheet.headers

        fetched_row = self.sheet.get(Comune="Acqui Terme")
        assert 'Codice Comune' not in fetched_row
        #self.sheet.append_column('Codice Comune')

    def test_adapter_rename_column(self):
        fetched_row = self.sheet.get(Comune="Acqui Terme")
        value = fetched_row['Codice Comune']

        self.sheet.rename_column("Codice Comune", "Postal Code")
        assert "Codice Comune" not in self.sheet.headers
        assert "Postal Code" in self.sheet.headers

        fetched_row = self.sheet.get(Comune="Acqui Terme")
        assert fetched_row['Postal Code'] == value

    def test_adapter_append_column(self):
        self.sheet.append_column("Maschi+Femmine", lambda r: r['Totale Maschi'] + r['Totale Femmine'])

        fetched_row = self.sheet.get(Comune="Acqui Terme")
        assert fetched_row["Maschi+Femmine"] == 20449

        self.sheet.append_column("test column")
        assert self.sheet.headers[-1] == 'test column' 
        fetched_row = self.sheet.get(Comune="Acqui Terme")
        assert fetched_row["test column"] == None

        self.sheet.append_column("test column 2", [1, 2, 3])
        fetched_rows = self.sheet.all()
        assert [row['test column 2'] for row in fetched_rows] == [1, 2, 3]

    def test_adapter_update_column(self):
        self.sheet.append_column("Maschi+Femmine", lambda r: None)

        fetched_row = self.sheet.get(Comune="Acqui Terme")
        assert fetched_row["Maschi+Femmine"] == None

        self.sheet.update_column("Maschi+Femmine", lambda r: r['Totale Maschi'] + r['Totale Femmine'])
        fetched_row = self.sheet.get(Comune="Acqui Terme")
        assert fetched_row["Maschi+Femmine"] == 20449

        filter_exp = lambda r: r['Comune'] == "Acqui Terme"
        def update_exp(r):
            r['Totale Maschi'] = 0
            return r
        self.sheet.update_rows(filter_exp, update_exp)

        fetched_row = self.sheet.get(Comune="Acqui Terme")
        assert fetched_row["Totale Maschi"] == 0

        self.sheet.update_column("Maschi+Femmine", lambda r: r['Totale Maschi'] + r['Totale Femmine'], filter_exp)
        fetched_row = self.sheet.get(Comune="Acqui Terme")
        assert fetched_row["Maschi+Femmine"] == 10939


class ShelveAdapterTestCase(BaseAdapterMixin, TestCase):
    workbook_class = shelve.ShelveBook

    def setup_book(self):
        return self.workbook_class(name='test_workbook', data_dir=TEST_DIR)

    def _test_shelve_adapter(self):
        assert os.path.exists(self.book.db)

    def tearDown(self):
        if os.path.exists(self.book.db):
            os.unlink(self.book.db)


class LocMemAdapterTestCase(BaseAdapterMixin, TestCase):
    workbook_class = locmem.LocMemBook

    def test_locmem_adapter(self):
        row = {
            "Codice Comune": 6001,
            "Comune": "Acqui Terme",
            "Totale Maschi": 9510,
            "Totale Femmine": 10939
        }
        doc = self.sheet._values_to_dict((6001, "Acqui Terme", 9510, 10939))
        assert doc == row
        values = self.sheet._dict_to_values(doc)
        assert values == (6001, "Acqui Terme", 9510, 10939)
