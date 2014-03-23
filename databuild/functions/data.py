def cross(book, row, sheet_source, column_source, column_key):
    """
    Returns a column from a different dataset, ordered as the key
    """
    a = book.sheets[sheet_source]

    return a.get(**{column_key: row[column_key]})[column_source]


def group_by(book):
    """
    groups a set of rows by column
    """
    raise NotImplementedError()

