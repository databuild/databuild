#!/usr/bin/env python
"""Naval Fate.

Usage:
  databuild.py <buildfile>
  databuild.py ship <buildfile> [--settings=<settings_path>]
  databuild.py (-h | --help)
  databuild.py --version

Options:
  -h --help     Show this screen.
  --version     Show version.
  --settings=<settings_path>  Use specified settings [default: databuild.settings].

"""
from docopt import docopt
from importlib import import_module
import json

from databuild import _version
from databuild.loader import load_classpath


def main(build_file, settings):
    settings = import_module(settings)
    AdapterClass = load_classpath(settings.ADAPTER) 
    
    book = AdapterClass()
    with open(build_file, 'rb') as fh:
        operations = json.load(fh)
        book.apply_operations(operations)


if __name__ == '__main__':
    arguments = docopt(__doc__, version='databuild v%s' % _version)
    main(arguments['<buildfile>'], settings=arguments['--settings'])
