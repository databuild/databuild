import os
from unittest import TestCase
from databuild import settings
from databuild.adapters.locmem.models import LocMemBook


TEST_DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')

settings.FUNCTIONS = list(settings.FUNCTIONS) + [
    'databuild.tests.functions',
]

class OperatorTestCase(TestCase):
    def test_operator(self):
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
        sheet = book.import_data('csv', os.path.join(TEST_DATA_DIR, "dataset1.csv"), sheet_name='dataset1', guess_types=False)
        sheet.append_column("test column")
        book.apply_operation(operation)
        assert sheet.get_column('test column')[0] == 'x'

    def test_function(self):
        operation = {
            "path": "columns.update_column",
            "description": "",
            "params": {
                "sheet": "dataset1",
                "column": "test column",
                "facets": [],
                "expression": {
                    "language": "python",
                    "content": "return test_fn()"
                }
            }
        }
        book = LocMemBook('project1')
        sheet = book.import_data('csv', os.path.join(TEST_DATA_DIR, "dataset1.csv"), sheet_name='dataset1', guess_types=False)
        sheet.append_column("test column")
        book.apply_operation(operation)
        assert sheet.get_column('test column')[0] == 'x'

    def test_function_map(self):
        operation = {
            "path": "columns.update_column",
            "description": "",
            "params": {
                "sheet": "a",
                "column": "test column",
                "facets": [],
                "expression": {
                    "language": "python",
                    "content": "return row['x'] * 10"
                }
            }
        }
        book = LocMemBook('project1')
        a_data = [
            {'id': 1, 'x': 2, 'y': 3},
            {'id': 2, 'x': 2, 'y': 3.5},
            {'id': 3, 'x': 1, 'y': 3.5},
        ]

        book = LocMemBook('project1')
        sheet_a = book.add_sheet('a', ['id', 'x', 'y'])

        sheet_a.extend(a_data)

        sheet_a.append_column("test column")
        book.apply_operation(operation)
        assert sheet_a.get_column('test column') == [20, 20, 10]

    def test_function_values(self):
        operation = {
            "path": "columns.update_column",
            "description": "",
            "params": {
                "sheet": "a",
                "column": "test column",
                "facets": [],
                "values": [
                    3,
                    5,
                    7
                ]
            }
        }
        book = LocMemBook('project1')
        a_data = [
            {'id': 1, 'x': 2, 'y': 3},
            {'id': 2, 'x': 2, 'y': 3.5},
            {'id': 3, 'x': 1, 'y': 3.5},
        ]

        book = LocMemBook('project1')
        sheet_a = book.add_sheet('a', ['id', 'x', 'y'])

        sheet_a.extend(a_data)

        sheet_a.append_column("test column")
        book.apply_operation(operation)
        assert sheet_a.get_column('test column') == [3, 5, 7]

    def test_cross_function(self):
        operation = {
            "path": "columns.update_column",
            "description": "",
            "params": {
                "sheet": "a",
                "column": "test column",
                "facets": [],
                "expression": {
                    "language": "python",
                    "content": "return cross(row, 'b', 'z', 'id')"
                }
            }
        }

        a_data = [
            {'id': 1, 'x': 2, 'y': 3},
            {'id': 2, 'x': 2, 'y': 3.5},
            {'id': 3, 'x': 1, 'y': 3.5},
        ]
        b_data = [
            {'id': 3, 'z': 3},
            {'id': 1, 'z': 4},
            {'id': 2, 'z': 4.5},
        ]

        book = LocMemBook('project1')
        sheet_a = book.add_sheet('a', ['id', 'x', 'y'])
        sheet_b = book.add_sheet('b', ['id', 'z'])

        sheet_a.extend(a_data)
        sheet_b.extend(b_data)

        sheet_a.append_column("test column")
        book.apply_operation(operation)
        assert sheet_a.get_column('test column') == [4, 4.5, 3]

    def test_column_function(self):
        operation = {
            "path": "columns.update_column",
            "description": "",
            "params": {
                "sheet": "a",
                "column": "test column",
                "facets": [],
                "expression": {
                    "language": "python",
                    "content": "zs = column('a', 'b', 'z', 'id'); return max(map(float, zs))"
                }
            }
        }

        a_data = [
            {'id': 1, 'x': 2, 'y': 3},
            {'id': 2, 'x': 2, 'y': 3.5},
            {'id': 3, 'x': 1, 'y': 3.5},
        ]
        b_data = [
            {'id': 3, 'z': 3},
            {'id': 1, 'z': 4},
            {'id': 2, 'z': 4.5},
        ]

        book = LocMemBook('project1')
        sheet_a = book.add_sheet('a', ['id', 'x', 'y'])
        sheet_b = book.add_sheet('b', ['id', 'z'])

        sheet_a.extend(a_data)
        sheet_b.extend(b_data)

        sheet_a.append_column("test column")
        book.apply_operation(operation)

        assert sheet_a.get_column('test column') == [4.5, 4.5, 4.5]

    def test_facets(self):
        operation = {
            "path": "columns.update_column",
            "description": "",
            "params": {
                "sheet": "dataset1",
                "column": "Totale Femmine",
                "facets": [
                    {
                        "expression": {
                            "language": "python",
                            "content": "return row['Comune'] == 'Acqui Terme'"
                        }
                    }
                ],
                "expression": {
                    "language": "python",
                    "content": "return 'x'"
                },
            }
        }

        book = LocMemBook('project1')
        sheet = book.import_data('csv', os.path.join(TEST_DATA_DIR, "dataset1.csv"), sheet_name='dataset1', guess_types=False)
        book.apply_operation(operation)
        assert sheet.get(Comune='Acqui Terme')['Totale Femmine'] == 'x'
        assert sheet.get(Comune='Albera Ligure')['Totale Femmine'] != 'x'
