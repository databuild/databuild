import os
from importlib import import_module

from databuild.loader import load_classpath
from databuild.buildfile import BuildFile
from databuild.utils import multiglob


def build(build_file_or_dir, settings='databuild.settings', echo=False):
    settings = import_module(settings)
    AdapterClass = load_classpath(settings.ADAPTER) 
    
    book = AdapterClass(settings=settings)
    if os.path.isfile(build_file_or_dir):
        build_files = [BuildFile(build_file_or_dir)]
    else:
        globs = (
            os.path.join(build_file_or_dir, "*.json"),
            os.path.join(build_file_or_dir, "*.yaml"),
            os.path.join(build_file_or_dir, "*.yml"),
        )
        build_files = map(BuildFile, sorted(multiglob(*globs)))
    book.apply_operations(build_files, echo)
    return book
