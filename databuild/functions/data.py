def cross(book, sheet, sheet_source, column_source, column_key):
    """
    Returns a column from a different dataset, ordered as the key
    """
    a = book.sheets[sheet_source]
    b = book.sheets[sheet]

    return [a.get(**{column_key: row[column_key]})[column_source] for row in b.all()]


def group_by(book):
    """
    groups a set of rows by column
    """
    raise NotImplementedError()

