import warnings
from databuild import settings
from databuild.loader import load_module
from lupa import LuaRuntime


def build_lua_runtime():
    lua_runtime = LuaRuntime()
    functions = []
    [functions.extend(load_module(module)) for module in settings.FUNCTIONS]

    lua_globals = lua_runtime.globals()

    for fn in functions:
        if not fn in lua_globals:
            lua_globals[fn.__name__] = fn
        else:
            warnings.warn("Function '%s' already present in Lua Environment. Skipping.")

    return lua_runtime

lua_runtime = build_lua_runtime()

def lua(expression, wrap=True):
    if wrap:
        func = 'function(row) %s end' % expression
    else:
        func = expression
    return lua_runtime.eval(func)
