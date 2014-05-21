.. _buildfiles

Buildfiles
----------

A ``buildfile`` contains a list of operations to be performed on data. Think of it as a script for a spreadsheet.

JSON and YAML format are supported. ``databuild`` will guess the format based on the file extension.

An example of build file could be::

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
        "description": "save the data",
        "params": {
          "sheet": "dataset1",
          "format": "csv",
          "filename": "dataset2.csv"
        }
      }
    ]

The same file in yaml::

    - function: sheets.import_data
      description: Importing data from csv file
      params: 
        sheet: dataset1
        format: csv
        filename: dataset1.csv
        skip_last_lines: 1
    - function: columns.add_column
      description: Calculate the gender ratio
      params: 
        sheet: dataset1
        name: Gender Ratio
        expression: 
          language: python
          content: "return float(row['Male Total']) / float(row['Female Totale'])"
    - function: sheets.export_data
      description: save the data
      params: 
        sheet: dataset1
        format: csv
        filename: dataset2.csv
