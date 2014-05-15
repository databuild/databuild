OPERATION_MODULES = (
    "databuild.operations.sheets",
    "databuild.operations.columns",
)

FUNCTIONS = (
    'databuild.functions.data',
)

ADAPTER = 'databuild.adapters.locmem.models.LocMemBook'

LANGUAGES = {
    'python': 'databuild.environments.python.PythonEnvironment',
}
