# Databuild

`make` for your data.

An automation tool for data manipulation.

Inspired by Open Refine.

## Installation

Requirements:

* Lua 5.1

### Linux

Install databuild:

```
  $ pip install git+https://github.com/fcurella/databuild.git
```

### OS X

Install Lua5.1 with `brew`:

```
  $ brew install lua
```

Download and extract databuild:

```
  $ wget https://github.com/fcurella/databuild/archive/master.tar.gz
  $ tar -zxf master.tar.gz -C databuild

```
Build:

```
  $ cd databuild
  $ make all
```

## Quickstart

```
$ data-build.py buildfile.json

```

`buildfile.json` contains a list of operations to be performed on data. Think of it as a script for a spreadsheet.

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
    "path": "columns.add_column",
    "description": "Calculate the gender ratio",
    "params": {
      "sheet": "dataset1",
      "name": "Gender Ratio",
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
```

For more, see the [Extended Documentation](http://databuild.readthedocs.org/en/latest/).

## License

Licensed under BSD 3-clauses.

## Status

This project is still in alpha stage.

## TODO

* R environment
* yaml buildfiles
