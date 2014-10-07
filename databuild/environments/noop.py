from .base import BaseEnvironment


class NoopEnvironment(BaseEnvironment):
    def __init__(self, book):
        super(NoopEnvironment, self).__init__(book)

    def copy(self, iterable):
        return iterable

    def eval(self, expression, context):
        return expression

