from datetime import datetime
from decimal import Decimal
import six
from unittest import TestCase

from databuild import functional

class FunctionalTestCase(TestCase):
    def test_compose(self):
        f1 = lambda x: x + 1
        f2 = lambda x: x + 2
        f3 = lambda x: x + 3

        fn = functional.compose(f1, f2, f3)
        assert fn(0) == 6

    def test_guess_type(self):
        values = [
            'Alice',
            'Bob',
            'Charlie',
            'Daniel',
            'Emily',
        ]
        assert functional.guess_type(values) == str

        values = [
            u'10939',
            u'157',
            u'49294',
            u'402',
            u'374',
        ]
        assert functional.guess_type(values) == int

        values = [
            '1',
            '2.5',
            '3.43',
            '4',
            '5.7',
        ]
        assert functional.guess_type(values) == float

        values = [
            '1.00',
            '2.50',
            '3.43',
            '4.00',
            '5.70',
        ]
        assert functional.guess_type(values) == Decimal

        values = [
            '2014-01-01',
            '2014-02-01',
            '2014-03-01',
            '2014-04-01',
            '2014-05-01',
        ]
        assert functional.guess_type(values) == datetime

        values = [
            '1',
            'Bob',
            '3.43',
            '2014-04-01',
            '5.70',
        ]
        assert functional.guess_type(values) == str

        values = [
            1,
            2,
            3,
            4,
            5,
        ]
        assert functional.guess_type(values) == int
