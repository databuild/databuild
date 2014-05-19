OPERATION_MODULES = (
    "databuild.operations.sheets",
    "databuild.operations.columns",
)

FUNCTION_MODULES = (
    'databuild.functions.data',
)

ADAPTER = 'databuild.adapters.locmem.models.LocMemBook'

LANGUAGES = {
    'python': 'databuild.environments.python.PythonEnvironment',
}
