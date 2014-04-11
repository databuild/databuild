import os
from unittest import TestCase
from databuild import settings
from databuild.adapters.locmem import LocMemBook


TEST_DIR = os.path.join(os.path.dirname(__file__))


class OperatorTestCase(TestCase):
    def test_update_column(self):
        operation = {
            "path": "columns.update_column",
            "description": "",
            "params": {
                "sheet": "dataset1",
                "column": "test column",
                "facets": [],
                "expression": {
                    "language": "python",
                    "content": "return 'x'"
                }
            }
        }
        book = LocMemBook('project1')
        sheet = book.import_data('csv', os.path.join(TEST_DIR, "dataset1.csv"), sheet_name='dataset1')
        sheet.append_column("test column")
        book.apply_operation(operation)
        assert sheet.get_column('test column')[0] == 'x'

    def test_import_data(self):
        operation = {
            "path": "core.import_data",
            "description": "Importing data from csv file",
            "params": {
              "sheet": "dataset1",
              "format": "csv",
              "filename": os.path.join(TEST_DIR, "dataset1.csv")
            }
        }

        book = LocMemBook('project1')
        book.apply_operation(operation)
        self.assertTrue('dataset1' in book.sheets)
