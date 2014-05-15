from unittest import TestCase
from databuild.adapters.locmem.models import LocMemBook


class ParserTestCase(TestCase):
    def test_parse_expression(self):
        expression = {"language": "python", "content": "return row['a']"}
        book = LocMemBook('project1')

        fn = book.operator.parse_expression(expression)
        row = {'a': 2}
        assert fn(row) == 2

        expression['content'] = 'import math; return math.pow(2, 2)'
        fn = book.operator.parse_expression(expression)
        assert fn(row) == 4
