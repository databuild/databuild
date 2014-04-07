Settings
========

``LANGUAGES``
-------------

A ``dict`` mapping languages to :doc:`environments`. Default to::

    LANGUAGES = {
        'lua': 'databuild.environments.lua.LuaEnvironment',
        'python': 'databuild.environments.python.PythonEnvironment',
    }
