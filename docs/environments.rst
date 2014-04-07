.. _environments

Environments
------------

:doc:expressions are evaluated in the environment specified by their ``language`` property.
The value maps to a specific environment as specified in ``settings.LANGUAGES``.

Currently, the following environments are shipped with ``databuild``.

Included Environments
=====================

Python
~~~~~~

**Unsafe** Python environment. Use only with trusted build files.


Lua
~~~

Requires Lua or LuaJIT (Note: LuaJIT is currently unsupported on OS X).


Writing Custom Environments
===========================

An ``Environment`` is a subclass of ``databuild.environments.base.BaseEnvironment``
that implementes the following methods:

    * ``__init__(self, book)``: Initializes the environment with the appropriate global variables.
    * ``copy(self, iterable)``: Copies a variable from the databuild process to the hosted environment.
    * ``eval(self, expression)``: Evaluates the string `expression` to an actual functions and returns it.
