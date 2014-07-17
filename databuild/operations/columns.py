from decimal import Decimal
from dateutil import parser as date_parser

import six


def update_column(context, sheet, column, facets=None, values=None, expression=None, wrap=True):
    assert values or expression

    workbook = context['workbook']
    callable_or_values = expression and expression or values
    sheet = workbook.sheets[sheet]
    sheet.update_column(column, callable_or_values, filter_fn=facets)


def add_column(context, sheet, name, expression=None):
    workbook = context['workbook']
    sheet = workbook.sheets[sheet]
    if expression is None:
        expression = lambda row: ''
    sheet.append_column(name, expression)


def remove_column(context, sheet, name):
    workbook = context['workbook']
    sheet = workbook.sheets[sheet]
    sheet.remove_column(name)


def rename_column(context, sheet, old_name, new_name):
    workbook = context['workbook']
    sheet = workbook.sheets[sheet]
    expression = lambda row: row[old_name]
    add_column(context, sheet, new_name, expression)
    sheet.remove_column(old_name)


def to_float(context, sheet, column, facets=None):
    expression = lambda x: float(x[column])
    update_column(context, sheet, column, facets, expression=expression)


def to_integer(context, sheet, column, facets=None):
    expression = lambda x: int(x[column])
    update_column(context, sheet, column, facets, expression=expression)


def to_decimal(context, sheet, column, facets=None):
    expression = lambda x: Decimal(x[column])
    update_column(context, sheet, column, facets, expression=expression)


def to_text(context, sheet, column, facets=None):
    expression = lambda x: six.text_type(x[column])
    update_column(context, sheet, column, facets, expression=expression)


def to_datetime(context, sheet, column, facets=None):
    expression = lambda x: date_parser.parse(x[column])
    update_column(context, sheet, column, facets, expression=expression)
