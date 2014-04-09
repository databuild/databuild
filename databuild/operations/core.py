def import_data(workbook, format, filename, sheet, headers=None, encoding='utf-8'):
    workbook.import_data(format, filename, sheet, headers, encoding)


def export_data(workbook, sheet, format, filename):
    sheet = workbook.sheets[sheet]
    data = sheet.export_data(format)
    with open(filename, 'wb') as fh:
        fh.write(data)


def print_data(workbook, sheet):
    sheet = workbook.sheets[sheet]
    sheet.print_data()
