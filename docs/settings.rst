.. _settings:

Settings
========

.. _adapter-setting:

``ADAPTER``
------------

Classpath of the adapter class. Defaults to ``'databuild.adapters.locmem.models.LocMemBook'``.

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


.. operation-modules-setting:

``OPERATION_MODULES``
---------------------

A ``tuple`` of module paths to import :doc:`operations` from. Defaults to::

    OPERATION_MODULES = (
        "databuild.operations.sheets",
        "databuild.operations.columns",
    )
