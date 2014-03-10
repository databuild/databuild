Quickstart
-----------

Install databuild::

  $ pip install git+https://github.com/fcurella/databuild.git

Run databuild using a buildfile::

  $ data-build.py buildfile.json

```

`buildfile.json` contains a list of operations to be performed on data. Think of it as a script for a spreadsheet.

An example of build file could be::

    [
      {
        "path": "core.import_data",
        "description": "Importing data from csv file",
        "params": {
          "sheet": "dataset1",
          "format": "csv",
          "filename": "dataset1.csv"
        }
      },
      {
        "path": "core.add_column",
        "description": "Calculate the gender ratio",
        "params": {
          "sheet": "dataset1",
          "column": "Gender Ratio",
          "facets": [],
          "expression": {
            "language": "lua",
            "content": "return row['Male Total'] / row['Female Total']"
          }
        }
      },
      {
        "path": "core.export_data",
        "description": "",
        "params": {
          "sheet": "dataset1",
          "format": "csv",
          "filename": "dataset2.csv"
        }
      }
    ]
