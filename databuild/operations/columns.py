def add_column(dataset, name='', expression=None):
    if expression is None:
        expression = lambda row: ''
    dataset.append_col(expression, header=name)


def remove_column(dataset, name):
    del dataset[name]


def rename_column(dataset, old_name, new_name):
    expression = lambda row: row[old_name]
    add_column(dataset, new_name, expression)
    remove_column(old_name)
