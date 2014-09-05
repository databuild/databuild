from __future__ import absolute_import
from databuild.operator import runtime_operations


def define_operation(context, name, operation, defaults):
    runtime_operations[name] = (operation, defaults)
