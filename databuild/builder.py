import os
from importlib import import_module

from databuild.loader import load_classpath
from databuild.buildfile import BuildFile
from databuild.utils import multiglob


class Builder(object):
    def __init__(self, settings='databuild.settings'):
        self.settings = import_module(settings)
        AdapterClass = load_classpath(self.settings.ADAPTER) 
        self.book = AdapterClass(settings=self.settings)
        super(Builder, self).__init__()
        
    def build(self, build_file_or_dir, echo=False):
        self.book.echo = echo

        if os.path.isfile(build_file_or_dir):
            build_files = [BuildFile(build_file_or_dir)]
        else:
            globs = (
                os.path.join(build_file_or_dir, "*.json"),
                os.path.join(build_file_or_dir, "*.yaml"),
                os.path.join(build_file_or_dir, "*.yml"),
            )
            build_files = map(BuildFile, sorted(multiglob(*globs)))
        self.book.apply_operations(build_files, echo=echo)
        return self.book
