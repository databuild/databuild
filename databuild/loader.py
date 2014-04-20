from importlib import import_module
from databuild import settings


def load_classpath(classpath):
    modules, function = classpath.rsplit('.', 1)
    if modules in settings.SHORTCUTS:
        modules = settings.SHORTCUTS[modules]

    module = import_module(modules)
    fn = getattr(module, function)
    return fn


def load_module(modulepath):
    module = import_module(modulepath)
    return [getattr(module, fn) for fn in dir(module) if not fn.startswith('_')]
