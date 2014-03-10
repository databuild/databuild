def transform(workbook, sheet, column, facets, expression, wrap=True):
    sheet = workbook.sheets[sheet]
    sheet.update_column(column, expression, filter_fn=facets)


def import_data(workbook, sheet, format, filename):
    workbook.import_data(format, filename, sheet)


def export_data(workbook, sheet, format, filename):
    sheet = workbook.sheets[sheet]
    sheet.export_data(format, filename)
