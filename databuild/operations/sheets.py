from databuild.compat import _open

def import_data(workbook, format, filename, sheet, *args, **kwargs):
    workbook.import_data(format, filename, sheet, *args, **kwargs)


def export_data(workbook, sheet, format, filename):
    sheet = workbook.sheets[sheet]
    data = sheet.export_data(format)
    with _open(filename, 'w', encoding='utf-8') as fh:
        fh.write(data)


def print_data(workbook, sheet):
    sheet = workbook.sheets[sheet]
    sheet.print_data()
