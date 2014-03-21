SHORTCUTS = {
    'core.import_data': "databuild.operations.core.import_data",
    'core.export_data': "databuild.operations.core.export_data",
    'core.print_data': "databuild.operations.core.print_data",
    'columns.add_column': "databuild.operations.columns.add_column",
    'columns.update_column': "databuild.operations.columns.update_column",
    'columns.remove_column': "databuild.operations.columns.remove_column",
    'columns.rename_column': "databuild.operations.columns.rename_column",
    'lua': "databuild.parsers.lua.lua",
}

FUNCTIONS = (
    'databuild.functions.data',
)

ADAPTER = 'databuild.adapters.locmem.LocMemBook'

LANGUAGES = {
    'lua': {
        'init': 'databuild.parsers.lua.build_lua_runtime',
        'parser': 'databuild.parsers.lua.lua'
    },
}