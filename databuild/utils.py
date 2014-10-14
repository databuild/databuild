import six

from glob import glob

from jinja2 import Template


def multiglob(*patterns):
    files_grabbed = []
    [files_grabbed.extend(glob(pattern)) for pattern in patterns]
    return files_grabbed


def render_string(tmpl, context):
    if tmpl:
        return Template(tmpl).render(**context)
    return ''


def recursive_render(value, context):
    if isinstance(value, list):
        return [recursive_render(v, context) for v in value]
    else:
        if value != 'description' and isinstance(value, six.string_types):
            return render_string(value, context)
    return value
