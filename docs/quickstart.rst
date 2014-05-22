.. _quickstart:

Quickstart
-----------

Run databuild using a :doc:`buildfile <buildfiles>`::

  $ data-build.py buildfile.json

``buildfile.json`` contains a list of operations to be performed on data. Think of it as a script for a spreadsheet.

An example of build file could be::

    [
      {
        "operation": "sheets.import_data",
        "description": "Importing data from csv file",
        "params": {
          "sheet": "dataset1",
          "format": "csv",
          "filename": "dataset1.csv",
          "skip_last_lines": 1
        }
      },
      {
        "operation": "columns.add_column",
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
        "operation": "sheets.export_data",
        "description": "save the data",
        "params": {
          "sheet": "dataset1",
          "format": "csv",
          "filename": "dataset2.csv"
        }
      }
    ]

YAML buildfiles are also supported. ``Databuild`` will guess the type based on the extension.
