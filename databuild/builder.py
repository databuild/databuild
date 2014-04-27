from importlib import import_module
import json

from databuild.loader import load_classpath


def build(build_file, settings='databuild.settings', echo=False):
    settings = import_module(settings)
    AdapterClass = load_classpath(settings.ADAPTER) 
    
    book = AdapterClass()
    with open(build_file, 'rb') as fh:
        operations = json.load(fh)
        book.apply_operations(operations, echo)
    return book
