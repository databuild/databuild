import six

if six.PY2:
    def _open(*args, **kwargs):
        kwargs.pop('encoding', False)
        return open(*args, **kwargs) 
else:
    _open = open
