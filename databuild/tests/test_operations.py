from datetime import datetime
from decimal import Decimal
import os
import six
from unittest import TestCase

from databuild.adapters.locmem.models import LocMemBook


TEST_DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')


class OperatorTestCase(TestCase):
    def test_update_column(self):
        operation = {
            "operation": "columns.update_column",
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
        sheet = book.import_data('csv', os.path.join(TEST_DATA_DIR, "dataset1.csv"), sheet_name='dataset1', guess_types=False)
        sheet.append_column("test column")
        book.apply_operation(operation)
        assert sheet.get_column('test column')[0] == 'x'

    def test_import_data(self):
        operation = {
            "operation": "sheets.import_data",
            "description": "Importing data from csv file",
            "params": {
              "sheet": "dataset1",
              "format": "csv",
              "filename": os.path.join(TEST_DATA_DIR, "dataset1.csv"),
              "skip_last_lines": 1
            }
        }

        book = LocMemBook('project1')
        book.apply_operation(operation)
        self.assertTrue('dataset1' in book.sheets)

    def test_to_float(self):
        operation = {
            "operation": "columns.to_float",
            "description": "",
            "params": {
                "sheet": "dataset1",
                "column": "Totale Maschi",
                "facets": []
            }
        }
        book = LocMemBook('project1')
        sheet = book.import_data('csv', os.path.join(TEST_DATA_DIR, "dataset1.csv"), sheet_name='dataset1', guess_types=False)
        book.apply_operation(operation)
        assert isinstance(sheet.get_column('Totale Maschi')[0], float)

    def test_to_integer(self):
        operation = {
            "operation": "columns.to_integer",
            "description": "",
            "params": {
                "sheet": "dataset1",
                "column": "Totale Maschi",
                "facets": []
            }
        }
        book = LocMemBook('project1')
        sheet = book.import_data('csv', os.path.join(TEST_DATA_DIR, "dataset1.csv"), sheet_name='dataset1', guess_types=False)
        book.apply_operation(operation)
        assert isinstance(sheet.get_column('Totale Maschi')[0], int)

    def test_to_decimal(self):
        operation = {
            "operation": "columns.to_decimal",
            "description": "",
            "params": {
                "sheet": "dataset1",
                "column": "Totale Maschi",
                "facets": []
            }
        }
        book = LocMemBook('project1')
        sheet = book.import_data('csv', os.path.join(TEST_DATA_DIR, "dataset1.csv"), sheet_name='dataset1', guess_types=False)
        book.apply_operation(operation)
        assert isinstance(sheet.get_column('Totale Maschi')[0], Decimal)

    def test_to_text(self):
        operation = {
            "operation": "columns.to_text",
            "description": "",
            "params": {
                "sheet": "dataset1",
                "column": "Totale Maschi",
                "facets": []
            }
        }
        book = LocMemBook('project1')
        sheet = book.import_data('csv', os.path.join(TEST_DATA_DIR, "dataset1.csv"), sheet_name='dataset1', guess_types=False)
        book.apply_operation(operation)
        assert isinstance(sheet.get_column('Totale Maschi')[0], six.text_type)

    def test_to_datetime(self):
        operation = {
            "operation": "columns.to_datetime",
            "description": "",
            "params": {
                "sheet": "dataset1",
                "column": "test column",
                "facets": []
            }
        }
        book = LocMemBook('project1')
        sheet = book.import_data('csv', os.path.join(TEST_DATA_DIR, "dataset1.csv"), sheet_name='dataset1', guess_types=False)
        sheet.append_column("test column", lambda x: '2014-01-01')
        book.apply_operation(operation)
        assert isinstance(sheet.get_column('test column')[0], datetime)

    def test_copy_sheet(self):
        operation = {
            "operation": "sheets.copy",
            "description": "",
            "params": {
                "source": "dataset1",
                "destination": "dataset2",
            }
        }
        book = LocMemBook('project1')
        sheet = book.import_data('csv', os.path.join(TEST_DATA_DIR, "dataset1.csv"), sheet_name='dataset1', guess_types=False)
        sheet.append_column("test column", lambda x: '2014-01-01')
        book.apply_operation(operation)
        assert 'dataset2' in book.sheets
        assert len(book.sheets['dataset2']) == len(book.sheets['dataset1'])
        assert len(book.sheets['dataset2'].headers) == len(book.sheets['dataset1'].headers)

        operation = {
            "operation": "sheets.copy",
            "description": "",
            "params": {
                "source": "dataset1",
                "destination": "dataset3",
                "headers": [
                    "Totale Maschi",
                    "Totale Femmine"
                ]
            }
        }
        book.apply_operation(operation)
        assert 'dataset3' in book.sheets
        assert len(book.sheets['dataset3']) == len(book.sheets['dataset1'])
        assert len(book.sheets['dataset3'].headers) < len(book.sheets['dataset1'].headers)
