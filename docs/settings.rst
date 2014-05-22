.. _settings:

Settings
========

.. _languages-setting:

``LANGUAGES``
-------------

A ``dict`` mapping languages to :doc:`environments`. Default to::

    LANGUAGES = {
        'python': 'databuild.environments.python.PythonEnvironment',
    }


.. _function-modules-setting:

``FUNCTION_MODULES``
--------------------

A ``tuple`` of module paths to import :doc:`functions` from. Defaults to::

    FUNCTION_MODULES = (
        'databuild.functions.data',
    )


``OPERATION_MODULES``
---------------------

A ``tuple`` of module paths to import :doc:`operations` from. Defaults to::

    OPERATION_MODULES = (
        "databuild.operations.sheets",
        "databuild.operations.columns",
    )
