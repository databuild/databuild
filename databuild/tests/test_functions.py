import os
from unittest import TestCase

from databuild.adapters.locmem import LocMemBook
from databuild.functions import data


TEST_DIR = os.path.join(os.path.dirname(__file__))

class FunctionsTestCase(TestCase):
    def test_cross(self):
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
        a = book.add_sheet('a', ['id', 'x', 'y'])
        b = book.add_sheet('b', ['id', 'z'])

        a.extend(a_data)
        b.extend(b_data)

        result = data.cross(book, 'a', 'b', 'z', 'id')
        assert result == [4, 4.5, 3]
