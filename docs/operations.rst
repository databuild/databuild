Operations
----------

Operations are functions called on the book. Examples of operations are: ``core.import_data``, ``columns.add_column``, ``columns.update_column``, and more.

They have a path that identifies them, an optional description and a number of parameters that they accept. Different operations have different parameters.

Available Operations
====================

``core.import_data``
~~~~~~~~~~~~~~~~~~~~

Creates a new sheet importing data from an external source.

arguments:
    * ``filename``: Required.
    * ``sheet``: Optional. Defaults to ``filename``'s basename.
    * ``format``: Values currently supported are ``'csv'`` and ``'json'``.
    * ``headers``: Optional. By default the importer tries to autodetects the header names.
    * ``encoding``: Optional. Defaults to ``'utf-8'``.

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
