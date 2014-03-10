from importlib import import_module
from databuild import settings


def load_classpath(classpath):
    if classpath in settings.SHORTCUTS:
        classpath = settings.SHORTCUTS[classpath]

    modules, function = classpath.rsplit('.', 1)
    module = import_module(modules)
    fn = getattr(module, function)
    return fn


def load_module(modulepath):
    module = import_module(modulepath)
    return [getattr(module, fn) for fn in dir(module) if not fn.startswith('_')]
