SHORTCUTS = {
    'core.import_data': "databuild.operations.core.import_data",
    'core.export_data': "databuild.operations.core.export_data",
    'core.print_data': "databuild.operations.core.print_data",
    'columns.add_column': "databuild.operations.columns.add_column",
    'columns.update_column': "databuild.operations.columns.update_column",
    'columns.remove_column': "databuild.operations.columns.remove_column",
    'columns.rename_column': "databuild.operations.columns.rename_column",
    'columns.to_float': "databuild.operations.columns.to_float",
    'columns.to_integer': "databuild.operations.columns.to_integer",
    'columns.to_text': "databuild.operations.columns.to_text",
}

FUNCTIONS = (
    'databuild.functions.data',
)

ADAPTER = 'databuild.adapters.locmem.LocMemBook'

LANGUAGES = {
    'python': 'databuild.environments.python.PythonEnvironment',
    'lua': 'databuild.environments.lua.LuaEnvironment',
}
