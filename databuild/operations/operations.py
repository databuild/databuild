from __future__ import absolute_import
from databuild.operator import runtime_operations, runtime_tasks


def define_operation(context, name, operation, description=None, defaults=None):
    if defaults is None:
        defaults = {}
    runtime_operations[name] = (operation, description, defaults)


def define_task(context, name, operations, description=None, defaults=None):
    if defaults is None:
        defaults = {}
    runtime_tasks[name] = (operations, description, defaults)


def call_task(context, name, description=None, overrides=None):
    workbook = context['workbook']
    buildfile = context['buildfile']
    if overrides is None:
        overrides = {}

    operations, description, defaults = runtime_tasks[name]
    for operation in operations:
        if 'params' not in operation:
            operation['params'] = {}
        operation['params'].update(defaults)
        operation['params'].update(overrides)
        workbook.apply_operation(operation, buildfile, context=context, echo=workbook.echo)
