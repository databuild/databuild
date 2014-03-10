import os
from unittest import TestCase
from databuild import settings
from databuild.adapters.locmem import LocMemBook


TEST_DIR = os.path.join(os.path.dirname(__file__))

settings.FUNCTIONS = list(settings.FUNCTIONS) + [
    'databuild.tests.functions',
]

class OperatorTestCase(TestCase):
    def test_operator(self):
        operation = {
            "path": "core.transform",
            "description": "",
            "params": {
                "sheet": "dataset1",
                "column": "test column",
                "facets": [],
                "expression": {
                    "language": "lua",
                    "content": "return 'x'"
                }
            }
        }
        book = LocMemBook('project1')
        sheet = book.import_data('csv', os.path.join(TEST_DIR, "dataset1.csv"), sheet_name='dataset1')
        sheet.append_column("test column")
        book.apply_operation(operation)
        assert sheet.get_column('test column')[0] == 'x'

    def test_function(self):
        operation = {
            "path": "core.transform",
            "description": "",
            "params": {
                "sheet": "dataset1",
                "column": "test column",
                "facets": [],
                "expression": {
                    "language": "lua",
                    "content": "return test_fn()"
                }
            }
        }
        book = LocMemBook('project1')
        sheet = book.import_data('csv', os.path.join(TEST_DIR, "dataset1.csv"), sheet_name='dataset1')
        sheet.append_column("test column")
        book.apply_operation(operation)
        assert sheet.get_column('test column')[0] == 'x'

    def test_facets(self):
        operation = {
            "path": "core.transform",
            "description": "",
            "params": {
                "sheet": "dataset1",
                "column": "Totale Femmine",
                "facets": [
                    {
                        "expression": {
                            "language": "lua",
                            "content": "return row['Comune'] == 'Acqui Terme'"
                        }
                    }
                ],
                "expression": {
                    "language": "lua",
                    "content": "return 'x'"
                },
            }
        }

        book = LocMemBook('project1')
        sheet = book.import_data('csv', os.path.join(TEST_DIR, "dataset1.csv"), sheet_name='dataset1')
        book.apply_operation(operation)
        assert sheet.get(Comune='Acqui Terme')['Totale Femmine'] == 'x'
        assert sheet.get(Comune='Albera Ligure')['Totale Femmine'] != 'x'
