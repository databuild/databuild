from databuild.facets import sum_facets
from databuild.loader import load_classpath
from databuild.parsers import parse_expression



class Operator(object):
    operations = []

    def __init__(self, workbook):
        self.workbook = workbook
        super(Operator, self).__init__()

    def apply_operation(self, operation, echo=False):
        if echo and operation['description']:
            print(operation['description'])

        fn = load_classpath(operation['path'])

        if 'expression' in operation['params']:
            operation['params']['expression'] = parse_expression(operation['params']['expression'])

        if 'facets' in operation['params']:
            facets = [parse_expression(facet['expression']) for facet in operation['params']['facets']]
            operation['params']['facets'] = sum_facets(facets)

        kwargs = operation['params']
        fn(self.workbook, **kwargs)
        self.operations.append(operation)
