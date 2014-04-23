SHORTCUTS = {
    'core': "databuild.operations.core",
    'columns': "databuild.operations.columns",
}

FUNCTIONS = (
    'databuild.functions.data',
)

ADAPTER = 'databuild.adapters.locmem.models.LocMemBook'

LANGUAGES = {
    'python': 'databuild.environments.python.PythonEnvironment',
    'lua': 'databuild.environments.lua.LuaEnvironment',
}
