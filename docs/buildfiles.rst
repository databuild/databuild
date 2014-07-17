.. _buildfiles:

Buildfiles
==========

A ``buildfile`` contains a list of operations to be performed on data. Think of it as a script for a spreadsheet.

JSON and YAML format are supported. ``databuild`` will guess the format based on the file extension.

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

The same file in yaml::

    - operation: sheets.import_data
      description: Importing data from csv file
      params: 
        sheet: dataset1
        format: csv
        filename: dataset1.csv
        skip_last_lines: 1
    - operation: columns.add_column
      description: Calculate the gender ratio
      params: 
        sheet: dataset1
        name: Gender Ratio
        expression: 
          language: python
          content: "return float(row['Male Total']) / float(row['Female Totale'])"
    - operation: sheets.export_data
      description: save the data
      params: 
        sheet: dataset1
        format: csv
        filename: dataset2.csv


You can split a buildfile in different files, and have ``databuild`` process the directory that contains them.

Build files will be executed in alphabetical order. It's recommended that you name them starting with a number indicating their order of execution. For example::

  ├── buildfiles
      ├── 1_import.json
      ├── 2_add_column.json
      ├── 3_export.json
      └── data
          └── dataset1.csv
