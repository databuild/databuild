.. _operations:

Operation Functions
===================

Operations functions are regular Python function that perform actions on the book. Examples of operations are: ``sheets.import_data``, ``columns.add_column``, ``columns.update_column``, and more.

They have a ``function`` name that identifies them, an optional description and a number of parameters that they accept. Different operation functions accept different parameters.

All operations accepts the following arguments:
    * ``name``: The name idnetifying the operation function
    * ``description``: Optional. A description to print on screen when the operation gets executed
    * ``params``: Parameter for the operation. This varies by operation. See below for a detailed list.
    * ``context``: Optional. An additional set of properties that can be made available to the operation. This can be used in expression or interpolated in strings (by using the ``{{ my var }}`` sysntax).
    * ``enabled``: Optional. Set this to ``False`` to skip execution of the operation. Useful for debug. Defaults to ``True``.

Available Operation Functions
-----------------------------

``sheets.import_data``
~~~~~~~~~~~~~~~~~~~~~~

Creates a new sheet importing data from an external source.

params:
    * ``filename``: Required.
    * ``sheet``: Optional. Defaults to ``filename``'s basename.
    * ``format``: Values currently supported are ``'csv'`` and ``'json'``.
    * ``headers``: Optional. Defaults to `null`, meaning that the importer tries to autodetects the header names.
    * ``encoding``: Optional. Defaults to ``'utf-8'``.
    * ``skip_first_lines``: Optional. Defaults to ``0``. Supported only by the CSV importer.
    * ``skip_Last_lines``: Optional. Defaults to ``0``. Supported only by the CSV importer.
    * ``guess_types``: Optional. If set to ``true``, the CSV importer will try to guess the data type. Defaults to ``true``.
    * ``replace``: Optional. if set to ``true`` and the sheet already exists, its content will be replaced. if set to ``false``, the new data will be appended. Defaults to ``false``.

``sheets.add``
~~~~~~~~~~~~~~~

params:
    * ``name``
    * ``headers`` (optional)

Adds a new empty sheet named ``name``. Optionally sets its headers as specified in ``headers``.

``sheets.copy``
~~~~~~~~~~~~~~~

params:
    * ``source``
    * ``destination``
    * ``headers`` (optional)

Create a copy of the ``source`` sheet named ``destination``. Optionally copies only the headers specified in ``headers``.

``sheets.export_data``
~~~~~~~~~~~~~~~~~~~~~~

params:
    * ``sheet``
    * ``format``
    * ``filename``
    * ``headers`` (optional)

Exports the datasheet named ``sheet`` to the file named ``filename`` in the specified ``format``. Optionally exports only the headers specified in ``headers``.

``sheets.print_data``
~~~~~~~~~~~~~~~~~~~~~

params:
    * ``sheet``

``columns.update_column``
~~~~~~~~~~~~~~~~~~~~~~~~~

params:
    * ``sheet``
    * ``column``
    * ``facets`` (optional)
    * ``values``
    * ``expression``

Either ``values`` or ``expression`` are required.

``columns.add_column``
~~~~~~~~~~~~~~~~~~~~~~

params:
    * ``sheet``
    * ``name``
    * ``values``
    * ``expression``

Either ``values`` or ``expression`` are required.

``columns.remove_column``
~~~~~~~~~~~~~~~~~~~~~~~~~

params:
    * ``sheet``
    * ``name``

``columns.rename_column``
~~~~~~~~~~~~~~~~~~~~~~~~~

params:
    * ``sheet``
    * ``old_name``
    * ``new_name``


``columns.to_float``
~~~~~~~~~~~~~~~~~~~~

params:
    * ``sheet``
    * ``column``
    * ``facets`` (optional)


``columns.to_integer``
~~~~~~~~~~~~~~~~~~~~~~

params:
    * ``sheet``
    * ``column``
    * ``facets`` (optional)


``columns.to_decimal``
~~~~~~~~~~~~~~~~~~~~~~

params:
    * ``sheet``
    * ``column``
    * ``facets`` (optional)


``columns.to_text``
~~~~~~~~~~~~~~~~~~~

params:
    * ``sheet``
    * ``column``
    * ``facets`` (optional)


``columns.to_datetime``
~~~~~~~~~~~~~~~~~~~~~~~

params:
    * ``sheet``
    * ``column``
    * ``facets`` (optional)

``system.call_command``
~~~~~~~~~~~~~~~~~~~~~~~

Calls an external command with the provided arguments.

params:
    * ``command``
    * ``arguments``

``operations.define_operation``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Define an alias to an operation with default params that can be reused.

params:
    * ``name``: how you want to name your operation. This is name that you will use to call the operation later.
    * ``operation``: the original path of the operation
    * ``defaults``: values that will be used as defaults for the operation. You can override them by using the ``params`` property when you call your operation

``operations.define_task``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Define an a task, a list of operations with default params that can be reused.

params:
    * ``name``: How you want to name your task. This is name that you will use to call the task later.
    * ``operations``: The operations to be applied
    * ``description``: Optional. A description to be printed when calling the task.
    * ``defaults``: Optional. values that will be used as defaults for the operations. You can override them by using the ``overrides`` param when you call your task

``operations.call_task``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Call a previously defined task

params:
    * ``name``: the name your task. This is name that you will use to call the operation later.
    * ``operations``: the operations to be applied
    * ``description``: Optional. A description to be printed when calling the task.
    * ``overrides``: values that will override the defaults for the operations.

Custom Operation
================

You can add your custom operation and use them in your buildfile.

An Operation is just a regular python function. The first arguments has to be the ``context``, but the remaining arguments will be pulled in from the ``params`` property of the operation in the buildfile.

By default, ``context`` is a ``dict`` with following keys:

* ``workbook``: a reference the workbook object
* ``buildfile``: a reference to the build file the operation has been read from.

::

    def myoperation(context, foo, bar, baz):
        pass

Operations are defined in modules, which are just regulare Python files.

As long as your operation modules are in your ``PYTHONPATH``, you can add them to your ``OPERATION_MODULES`` setting (see :ref:`operation-modules-setting`) and then call the operation in your buildfile by referencing its import path::

    [
        ...,
        {
            "operation": "mymodule.myoperation",
            "description": "",
            "params": {
                "foo": "foos",
                "bar": "bars",
                "baz": "bazes"
            }
        }
    ]
