from glob import glob
import os
from importlib import import_module

from databuild.loader import load_classpath


def build(build_file_or_dir, settings='databuild.settings', echo=False):
    settings = import_module(settings)
    AdapterClass = load_classpath(settings.ADAPTER) 
    
    book = AdapterClass(settings=settings)
    if os.path.isfile(build_file_or_dir):
        build_files = [build_file_or_dir]
    else:
        build_files = sorted(glob("%s/*.json" % build_file_or_dir))
    book.apply_operations(build_files, echo)
    return book
