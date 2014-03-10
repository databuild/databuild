# Databuild

`make` for your data.

An automation tool for data manipulation.

Inspired by Open Refine.

## Quickstart

```
$ databuild makefile.json

```

`makefile.json` contains a list of operations to be performed on data. Think of it as a script for a spreadsheet.

An example of build file could be:

```
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
        "content": "return row['Totale Maschi'] / row['Totale Femmine']"
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
```
## Data Model

Data is organized in a `Workbook`, containing one or more `Sheet`s.

## Operations

Operations are functions called on the book. Examples of operations are: `core.import_data`, `core.add_column`, `core.transform`, and more.

They have a path that identifies them, an optional description and a number of parameters that they accept. Different operations have different parameters.

## Expressions

Expressions are objects representing code for complex situations, such as filtering or calculations.

## Functions

## Extending

## License

Licensed under BSD 3-clauses.

## TODO

* custom settings
* exporting for ShelveSheet
* R environment
* yaml buildfiles
