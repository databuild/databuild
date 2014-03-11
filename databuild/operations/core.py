def import_data(workbook, sheet, format, filename):
    workbook.import_data(format, filename, sheet)


def export_data(workbook, sheet, format, filename):
    sheet = workbook.sheets[sheet]
    data = sheet.export_data(format)
    with open(filename, 'wb') as fh:
        fh.write(data)

