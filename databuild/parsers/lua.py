import functools
import warnings
from databuild import settings
from databuild.loader import load_module
from lupa import LuaRuntime

from .base import BaseEnvironment

class LuaEnvironment(BaseEnvironment):
    def __init__(self, book):
        lua_runtime = LuaRuntime()
        functions = []
        [functions.extend(load_module(module)) for module in settings.FUNCTIONS]

        lua_globals = lua_runtime.globals()

        for fn in functions:
            if not fn in lua_globals:
                lua_globals[fn.__name__] = functools.partial(fn, book)
            else:
                warnings.warn("Function '%s' already present in Lua Environment. Skipping.")

        self.runtime = lua_runtime
        super(LuaEnvironment, self).__init__(book)


    def eval(self, expression, wrap=True):
        if wrap:
            func = 'function(row) %s end' % expression
        else:
            func = expression

        return self.runtime.eval(func)
