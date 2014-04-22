Operation Functions
-------------------

Operations functions are regular Python function that perform actions on the book. Examples of operations are: ``core.import_data``, ``columns.add_column``, ``columns.update_column``, and more.

They have a path that identifies them, an optional description and a number of parameters that they accept. Different operation functions accept different parameters.

Available Operation Functions
=============================

``core.import_data``
~~~~~~~~~~~~~~~~~~~~

Creates a new sheet importing data from an external source.

arguments:
    * ``filename``: Required.
    * ``sheet``: Optional. Defaults to ``filename``'s basename.
    * ``format``: Values currently supported are ``'csv'`` and ``'json'``.
    * ``headers``: Optional. Defaults to `null`, meaning that the importer tries to autodetects the header names.
    * ``encoding``: Optional. Defaults to ``'utf-8'``.
    * ``skip_first_lines``: Optional. Defaults to ``0``. Supported only be the CSV importer.
    * ``skip_Last_lines``: Optional. Defaults to ``0``. Supported only be the CSV importer.
    * ``guess_types``: Optional. If set to ``true``, the CSV importer will try to guess the data type. Defaults to ``true``.

``core.export_data``
~~~~~~~~~~~~~~~~~~~~

arguments:
    * ``sheet``
    * ``format``
    * ``filename``


``core.print_data``
~~~~~~~~~~~~~~~~~~~~

arguments:
    * ``sheet``

``columns.update_column``
~~~~~~~~~~~~~~~~~~~~~~~~~

arguments:
    * ``sheet``
    * ``column``
    * ``facets``
    * ``expression``
    * ``values``

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

Custom Operation Functions
===========================

You can add your custom operation functions and use them in your buildfile.

An Operation Function is just a regular python function. The first arguments has to be the ``workbook``, but the remaining arguments will be pulled in from the ``params`` property of the operation in the buildfile.

::

    def myoperation(workbook, foo, bar, baz):
        pass

As long as your operation function is in your ``PYTHONPATH``, you can call it in your buildfile by referincing its import path::

    [
        ...,
        {
            "path": "mymodule.myoperation",
            "description": "",
            "params": {
                "foo": "foos",
                "bar": "bars",
                "baz": "bazes"
            }
        }
    ]
