import os
from unittest import TestCase
from databuild import settings

from databuild.adapters.locmem.models import LocMemBook
from databuild.functions import data


TEST_DIR = os.path.join(os.path.dirname(__file__))

settings.LANGUAGES['noop'] = 'databuild.environments.noop.NoopEnvironment'


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
        env = book.operator.languages['noop']

        a = book.add_sheet('a', ['id', 'x', 'y'])
        b = book.add_sheet('b', ['id', 'z'])

        a.extend(a_data)
        b.extend(b_data)

        result = [data.cross(env, book, row, 'b', 'z', 'id') for row in a.all()]
        assert result == [4, 4.5, 3]

    def test_column(self):
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
        env = book.operator.languages['noop']

        a = book.add_sheet('a', ['id', 'x', 'y'])
        b = book.add_sheet('b', ['id', 'z'])

        a.extend(a_data)
        b.extend(b_data)

        result = data.column(env, book, 'a', 'b', 'z', 'id')
        assert result == [4, 4.5, 3]
