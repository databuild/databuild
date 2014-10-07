#!/usr/bin/env python
"""data-build.

Usage:
  databuild.py <buildfile>
  databuild.py <buildfile> [--settings=<settings_path>]
  databuild.py (-h | --help)
  databuild.py --version

Options:
  -h --help     Show this screen.
  --version     Show version.
  --settings=<settings_path>  Use specified settings [default: databuild.settings].

"""
from docopt import docopt

from databuild import _version
from databuild.builder import Builder


def main(build_file, settings):
    builder = Builder(settings)
    builder.build(build_file, echo=True)


if __name__ == '__main__':
    arguments = docopt(__doc__, version='databuild v%s' % _version)
    main(arguments['<buildfile>'], settings=arguments['--settings'])
