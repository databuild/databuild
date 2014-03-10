import os
from unittest import TestCase
from databuild.parsers import parse_expression


TEST_DIR = os.path.join(os.path.dirname(__file__))

class ParserTestCase(TestCase):
    def test_parse_expression(self):
        expression = {"language": "lua", "content": "return row['a']"}

        fn = parse_expression(expression)
        row = {'a': 2}
        assert fn(row) == 2

        expression['content'] = 'return math.pow(2, 2)'
        fn = parse_expression(expression)
        assert fn() == 4