from datetime import datetime
from dateutil import parser as dateparser
from decimal import Decimal
from functools import partial
import six

 
def _composed(f, g, *args, **kwargs):
    return f(g(*args, **kwargs))
 

def compose(*a):
    try:
        return partial(_composed, a[0], compose(*a[1:]))
    except IndexError:
        return a[0]


def _type_check(values, value_type, check_fn=None, exception=ValueError):
    if check_fn is None:
        check_fn = value_type

    type_check = True
    for value in values:
        try:
            check_fn(value)
        except exception:
            type_check = False
            break

    if type_check:
        return value_type
    return None


def guess_type(values):
    decimal_points = ['.' in value for value in values if isinstance(value, six.string_types) and '.' in value]

    if decimal_points:
        if len(decimal_points) == len(values):
            decimal_parts = set([len(value.rsplit('.', 1)[1]) for value in values])
            if len(decimal_parts) == 1:
                return Decimal

        value_type = _type_check(values, float)
        if value_type:
            return value_type

    value_type = _type_check(values, int)
    if value_type:
        return value_type


    value_type = _type_check(values, datetime, dateparser.parse, TypeError)
    if value_type:
        return value_type

    types = set([value.__class__ for value in values])
    if len(types) == 1:
        return types.pop()
    return six.string_types[0]
