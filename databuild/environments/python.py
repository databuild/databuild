import functools
import warnings

from databuild.loader import load_module

from .base import BaseEnvironment


def indent(s, numSpaces):
    lines = s.splitlines()
    s = [(numSpaces * ' ') + line for line in lines]
    return '\n'.join(s)


class PythonEnvironment(BaseEnvironment):
    def __init__(self, book):
        globs = globals()

        self.globals = {}

        functions = []
        [functions.extend(load_module(module)) for module in book.settings.FUNCTIONS]

        for fn in functions:
            if fn.__name__ not in globs:
                self.globals[fn.__name__] = functools.partial(fn, self, book)
            else:
                warnings.warn("Function '%s' already present in Python Environment. Skipping.")

        super(PythonEnvironment, self).__init__(book)

    def copy(self, iterable):
        return iterable

    def eval(self, expression):
        expression = "def fn(row):\n%s\n" % indent(expression, 4)
        exec(expression, self.globals, locals())
        return vars()['fn']

