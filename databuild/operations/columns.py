def update_column(workbook, sheet, column, facets, values=None, expression=None, wrap=True):
    assert values or expression

    callable_or_values = expression and expression or values
    sheet = workbook.sheets[sheet]
    sheet.update_column(column, callable_or_values, filter_fn=facets)


def add_column(workbook, sheet, name, expression=None):
    sheet = workbook.sheets[sheet]
    if expression is None:
        expression = lambda row: ''
    sheet.append_column(name, expression)


def remove_column(workbook, sheet, name):
    sheet = workbook.sheets[sheet]
    sheet.remove_column(name)


def rename_column(workbook, sheet, old_name, new_name):
    sheet = workbook.sheets[sheet]
    expression = lambda row: row[old_name]
    add_column(workbook, sheet, new_name, expression)
    sheet.remove_column(old_name)
