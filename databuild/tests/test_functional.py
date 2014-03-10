from unittest import TestCase

from databuild import functional

class FunctionalTestCase(TestCase):
    def test_compose(self):
        f1 = lambda x: x + 1
        f2 = lambda x: x + 2
        f3 = lambda x: x + 3

        fn = functional.compose(f1, f2, f3)
        assert fn(0) == 6
