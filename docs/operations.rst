.. _operations:

Operation Functions
===================

Operations functions are regular Python function that perform actions on the book. Examples of operations are: ``sheets.import_data``, ``columns.add_column``, ``columns.update_column``, and more.

They have a ``function`` name that identifies them, an optional description and a number of parameters that they accept. Different operation functions accept different parameters.

Available Operation Functions
-----------------------------

``sheets.import_data``
~~~~~~~~~~~~~~~~~~~~~~

Creates a new sheet importing data from an external source.

arguments:
    * ``filename``: Required.
    * ``sheet``: Optional. Defaults to ``filename``'s basename.
    * ``format``: Values currently supported are ``'csv'`` and ``'json'``.
    * ``headers``: Optional. Defaults to `null`, meaning that the importer tries to autodetects the header names.
    * ``encoding``: Optional. Defaults to ``'utf-8'``.
    * ``skip_first_lines``: Optional. Defaults to ``0``. Supported only by the CSV importer.
    * ``skip_Last_lines``: Optional. Defaults to ``0``. Supported only by the CSV importer.
    * ``guess_types``: Optional. If set to ``true``, the CSV importer will try to guess the data type. Defaults to ``true``.

``sheets.copy``
~~~~~~~~~~~~~~~

arguments:
    * ``source``
    * ``destination``
    * ``headers`` (optional)

Create a copy of the ``source`` sheet named ``destination``. Optionally copies only the headers specified in ``headers``.

``sheets.export_data``
~~~~~~~~~~~~~~~~~~~~~~

arguments:
    * ``sheet``
    * ``format``
    * ``filename``
    * ``headers`` (optional)

Exports the datasheet named ``sheet`` to the file named ``filename`` in the specified ``format``. Optionally exports only the headers specified in ``headers``.

``sheets.print_data``
~~~~~~~~~~~~~~~~~~~~~

arguments:
    * ``sheet``

``columns.update_column``
~~~~~~~~~~~~~~~~~~~~~~~~~

arguments:
    * ``sheet``
    * ``column``
    * ``facets`` (optional)
    * ``values``
    * ``expression``

Either ``values`` or ``expression`` are required.

``columns.add_column``
~~~~~~~~~~~~~~~~~~~~~~

arguments:
    * ``sheet``
    * ``name``
    * ``expression`` (optional)

``columns.remove_column``
~~~~~~~~~~~~~~~~~~~~~~~~~

arguments:
    * ``sheet``
    * ``name``

``columns.rename_column``
~~~~~~~~~~~~~~~~~~~~~~~~~

arguments:
    * ``sheet``
    * ``old_name``
    * ``new_name``


``columns.to_float``
~~~~~~~~~~~~~~~~~~~~

arguments:
    * ``sheet``
    * ``column``
    * ``facets`` (optional)


``columns.to_integer``
~~~~~~~~~~~~~~~~~~~~~~

arguments:
    * ``sheet``
    * ``column``
    * ``facets`` (optional)


``columns.to_decimal``
~~~~~~~~~~~~~~~~~~~~~~

arguments:
    * ``sheet``
    * ``column``
    * ``facets`` (optional)


``columns.to_text``
~~~~~~~~~~~~~~~~~~~

arguments:
    * ``sheet``
    * ``column``
    * ``facets`` (optional)


``columns.to_datetime``
~~~~~~~~~~~~~~~~~~~~~~~

arguments:
    * ``sheet``
    * ``column``
    * ``facets`` (optional)

``operations.define_operation``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Define an alias to an operation with default arguments that can be reused.

arguments:
    * ``name``: how you want to name your operation. This is name that you will use to call the operation later.
    * ``operation``: the original path of the operation
    * ``defaults``: values that will be used as defaults for the operation. You can override them by using the ``params`` property when you call your operation

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
