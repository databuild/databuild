def cross(environment, book, row, sheet_source, column_source, column_key):
    """
    Returns a value from a column from a different dataset, matching by the key.
    """
    a = book.sheets[sheet_source]

    return environment.copy(a.get(**{column_key: row[column_key]})[column_source])


def column(environment, book, sheet, sheet_source, column_source, column_key):
    """
    Returns an array of values from column from a different dataset, ordered as the key.
    """
    a = book.sheets[sheet_source]
    b = book.sheets[sheet]

    return environment.copy([a.get(**{column_key: row[column_key]})[column_source] for row in b.all()])
