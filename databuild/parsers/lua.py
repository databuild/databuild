import functools
import warnings
from databuild import settings
from databuild.loader import load_module
from lupa import LuaRuntime


def build_lua_runtime(book):
    lua_runtime = LuaRuntime()
    functions = []
    [functions.extend(load_module(module)) for module in settings.FUNCTIONS]

    lua_globals = lua_runtime.globals()

    for fn in functions:
        if not fn in lua_globals:
            lua_globals[fn.__name__] = functools.partial(fn, book)
        else:
            warnings.warn("Function '%s' already present in Lua Environment. Skipping.")

    return lua_runtime


def lua(runtime, expression, wrap=True):
    if wrap:
        func = 'function(row) %s end' % expression
    else:
        func = expression

    return runtime.eval(func)
