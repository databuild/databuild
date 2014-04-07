from databuild.facets import sum_facets
from databuild.loader import load_classpath

from databuild import settings



class Operator(object):
    operations = []

    def __init__(self, workbook):
        self.workbook = workbook
        self.languages = self.build_languages()

        super(Operator, self).__init__()

    def build_languages(self):
        languages = {}
        for name, runtime in settings.LANGUAGES.items():
            RuntimeClass = load_classpath(runtime)
            languages[name] = RuntimeClass(self.workbook)
        return languages

    def apply_operation(self, operation, echo=False):
        if echo and operation['description']:
            print(operation['description'])

        fn = load_classpath(operation['path'])

        if 'expression' in operation['params']:
            operation['params']['expression'] = self.parse_expression(operation['params']['expression'])

        if 'facets' in operation['params']:
            facets = [self.parse_expression(facet['expression']) for facet in operation['params']['facets']]
            operation['params']['facets'] = sum_facets(facets)

        kwargs = operation['params']
        fn(self.workbook, **kwargs)
        self.operations.append(operation)

    def parse_expression(self, expression):
        language, exp = expression['language'], expression['content']
        runtime = self.languages[language]
        return runtime.eval(exp)

def column_reference(reference):
    """
    "sheet"."column"
    "sheet \"escaped quotes\""."column"
    "sheet name.something"."column"
    'sheet name.something'.'column'
    """
    quote = reference[0]
    split_token = "{0}.{0}".format(quote)
    sheet, column = reference[1:-1].split(split_token)
    sheet = sheet.replace('\%s' % quote, quote)
    column = column.replace('\%s' % quote, quote)
    sheet = sheet.replace('\\\\', '\\')
    column = column.replace('\\\\', '\\')
    return sheet.column
