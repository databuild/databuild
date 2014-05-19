.. _functions:

Functions
---------

Functions are additional methods that can be used inside :doc:`expressions`.

Available Functions
===================

``cross``
~~~~~~~~~

Return data from a column in a different sheet.

arguments:
    * ``row`` reference to the current row
    * ``sheet_source`` name of the sheet that you want to get the data from
    * ``column_source`` name of the column that you want to get the data from
    * ``column_key`` name of the sheet that you want to match the data between the sheets.

``column``


Custom Functions Modules
========================

You can write your own custom functions modules.

A function module is a regulare Python module containing Python functions with the following signature::

    def myfunction(environment, book, **kwargs)

Function must accept the ``environment`` and ``book`` positional arguments. After them, everything other argument is up the the function.

Another reuqirement is that the function must return a value wrapped into the environment's copy method::

    return environment.copy(my_return_value)

Function modules must be made available by adding them to the ``FUNCTION_MODULES`` :doc:`settings` variable.
