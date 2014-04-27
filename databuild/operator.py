import json
import os

from databuild.compat import _open
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
            try:
                RuntimeClass = load_classpath(runtime)
            except ImportError:
                continue
            else:
                languages[name] = RuntimeClass(self.workbook)
        return languages

    def apply_operations(self, build_file, echo=False):
        self.build_file = os.path.abspath(build_file)

        with _open(build_file, 'rb', encoding='utf-8') as fh:
            operations = json.load(fh)
            [self.apply_operation(op, echo) for op in operations]

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
