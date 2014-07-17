from databuild.compat import _open

def import_data(context, format, filename, sheet, *args, **kwargs):
    workbook = context['workbook']
    if context['buildfile']:
        relative_path = context['buildfile'].parent_dir
    else:
        relative_path = None
    workbook.import_data(filename, relative_path=relative_path, format=format, sheet_name=sheet, *args, **kwargs)


def export_data(context, sheet, format, filename, headers=None):
    workbook = context['workbook']
    sheet = workbook.sheets[sheet]
    data = sheet.export_data(format=format, headers=headers)
    with _open(filename, 'w', encoding='utf-8') as fh:
        fh.write(data)


def print_data(context, sheet):
    workbook = context['workbook']
    sheet = workbook.sheets[sheet]
    sheet.print_data()


def copy(context, source, destination, headers=None):
    workbook = context['workbook']
    sheet = workbook.sheets[source]
    sheet.copy(destination, headers)
