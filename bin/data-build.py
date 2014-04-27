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
from databuild.builder import build


def main(build_file, settings):
    build(build_file, settings, echo=True)


if __name__ == '__main__':
    arguments = docopt(__doc__, version='databuild v%s' % _version)
    main(arguments['<buildfile>'], settings=arguments['--settings'])
