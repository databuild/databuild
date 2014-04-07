class BaseEnvironment(object):
    def __init__(self, book):
        """
        Initializes the environment with the appropriate global variables.
        """
        super(BaseEnvironment, self).__init__()

    def copy(self, iterable):
        """
        Copies a variable from the databuild process to the hosted environment.
        """
        raise NotImplementedError()

    def eval(self, expression):
        """
        Evaluates the string `expression` to an actual functions and returns it.
        """
        raise NotImplementedError()
