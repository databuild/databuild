class BaseEnvironment(object):
    def __init__(self, book):
        super(BaseEnvironment, self).__init__()

    def eval(self, expression, wrap=True):
        raise NotImplementedError()
