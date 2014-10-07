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