import os
from unittest import TestCase
from databuild.adapters.locmem import LocMemBook


TEST_DIR = os.path.join(os.path.dirname(__file__))


class ParserTestCase(TestCase):
    def test_parse_expression(self):
        expression = {"language": "lua", "content": "return row['a']"}
        book = LocMemBook('project1')

        fn = book.operator.parse_expression(expression)
        row = {'a': 2}
        assert fn(row) == 2

        expression['content'] = 'return math.pow(2, 2)'
        fn = book.operator.parse_expression(expression)
        assert fn() == 4
