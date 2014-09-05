from __future__ import absolute_import
from databuild.operator import runtime_operations


def define_operation(context, name, operation, description=None, defaults=None):
    if defaults is None:
        defaults = {}
    runtime_operations[name] = (operation, description, defaults)
