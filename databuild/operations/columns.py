def update_column(workbook, sheet, column, facets, expression, wrap=True):
    sheet = workbook.sheets[sheet]
    sheet.update_column(column, expression, filter_fn=facets)


def add_column(workbook, sheet, name='', expression=None):
    sheet = workbook.sheets[sheet]
    if expression is None:
        expression = lambda row: ''
    sheet.append_col(expression, header=name)


def remove_column(workbook, sheet, name):
    sheet = workbook.sheets[sheet]
    sheet.remove_column(name)


def rename_column(workbook, sheet, old_name, new_name):
    sheet = workbook.sheets[sheet]
    expression = lambda row: row[old_name]
    add_column(workbook, sheet, new_name, expression)
    sheet.remove_column(old_name)
