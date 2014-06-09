Databuild
=========

``make`` for your data.

An automation tool for data manipulation.

Inspired by Open Refine.

The general principles in ``Databuild`` are:

* Low entry barrier
* Easy to install
* Easy to grasp
* Extensible

Databuild can be useful for scenarios such as:

* Documenting data transformations in your infoviz project
* Automate data processing in a declarative way

Installation
------------

Install databuild:

::

      $ pip install databuild

Quickstart
----------

For more details, see the `Extended Documentation`_.

::

    $ data-build.py buildfile.json

``buildfile.json`` contains a list of operations to be performed on
data. Think of it as a script for a spreadsheet.

An example of build file could be:

.. code:: json

    [
      {
        "function": "sheets.import_data",
        "description": "Importing data from csv file",
        "params": {
          "sheet": "dataset1",
          "format": "csv",
          "filename": "dataset1.csv",
          "skip_last_lines": 1
        }
      },
      {
        "function": "columns.add_column",
        "description": "Calculate the gender ratio",
        "params": {
          "sheet": "dataset1",
          "name": "Gender Ratio",
          "expression": {
            "language": "python",
            "content": "return float(row['Male Total']) / float(row['Female Total'])"
          }
        }
      },
      {
        "function": "sheets.export_data",
        "description": "",
        "params": {
          "sheet": "dataset1",
          "format": "csv",
          "filename": "dataset2.csv"
        }
      }
    ]

YAML buildfiles are also supported. ``databuild`` will guess the type
based on the extension.

License
-------

Licensed under BSD 3-clauses.

.. _Extended Documentation: http://databuild.readthedocs.org/en/latest/
