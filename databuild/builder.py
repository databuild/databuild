from importlib import import_module

from databuild.loader import load_classpath


def build(build_file, settings='databuild.settings', echo=False):
    settings = import_module(settings)
    AdapterClass = load_classpath(settings.ADAPTER) 
    
    book = AdapterClass(settings=settings)
    book.apply_operations(build_file, echo)
    return book
