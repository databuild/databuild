ADAPTER = 'databuild.adapters.locmem.models.LocMemBook'

FUNCTION_MODULES = (
    'databuild.functions.data',
)

LANGUAGES = {
    'python': 'databuild.environments.python.PythonEnvironment',
}

OPERATION_MODULES = (
    "databuild.operations.sheets",
    "databuild.operations.columns",
    "databuild.operations.operations",
    "databuild.operations.system",
)
