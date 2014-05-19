.. _settings

Settings
========

``LANGUAGES``
-------------

A ``dict`` mapping languages to :doc:environments. Default to::

    LANGUAGES = {
        'python': 'databuild.environments.python.PythonEnvironment',
        'lua': 'databuild.environments.lua.LuaEnvironment',
    }

``FUNCTION_MODULES``
--------------------