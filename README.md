# Databuild

`make` for your data.

An automation tool for data manipulation.

Inspired by Open Refine.

## Installation

Install databuild:

```
  $ pip install https://github.com/databuild/databuild/archive/master.tar.gz
```

## Quickstart

For more details, see the [Extended Documentation](http://databuild.readthedocs.org/en/latest/).

```
$ data-build.py buildfile.json

```

`buildfile.json` contains a list of operations to be performed on data. Think of it as a script for a spreadsheet.

An example of build file could be:

```json
[
  {
    "path": "sheets.import_data",
    "description": "Importing data from csv file",
    "params": {
      "sheet": "dataset1",
      "format": "csv",
      "filename": "dataset1.csv",
      "skip_last_lines": 1
    }
  },
  {
    "path": "columns.add_column",
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
    "path": "sheets.export_data",
    "description": "",
    "params": {
      "sheet": "dataset1",
      "format": "csv",
      "filename": "dataset2.csv"
    }
  }
]
```

YAML buildfiles are also supported. `databuild` will guess the type based on the extension.

## License

Licensed under BSD 3-clauses.

## Status

This project is still in alpha stage.

## TODO

* pandas adapter
* R environment
* split buildfiles