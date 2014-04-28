from importlib import import_module


def load_classpath(classpath):
    modules, function = classpath.rsplit('.', 1)
    module = import_module(modules)
    fn = getattr(module, function)
    return fn


def load_classpath_whitelist(classpath, whitelist=None, shortcuts=False):
    modules, function = classpath.rsplit('.', 1)
    if shortcuts:
        names = dict([(path.rsplit('.', 1)[1], path) for path in whitelist])
        if modules in names:
            modules = names[modules]

    if whitelist is None or modules in whitelist:
        module = import_module(modules)
        return getattr(module, function)
    raise ImportError


def load_module(modulepath):
    module = import_module(modulepath)
    return [getattr(module, fn) for fn in dir(module) if not fn.startswith('_')]
