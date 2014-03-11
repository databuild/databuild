Operations
----------

Operations are functions called on the book. Examples of operations are: ``core.import_data``, ``columns.add_column``, ``columns.update_column``, and more.

They have a path that identifies them, an optional description and a number of parameters that they accept. Different operations have different parameters.

Available Operations
====================

``core.import_data``
~~~~~~~~~~~~~~~~~~~~

arguments:
    * ``sheet``
    * ``format``
    * ``filename``

``core.export_data``
~~~~~~~~~~~~~~~~~~~~

arguments:
    * ``sheet``
    * ``format``
    * ``filename``

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
