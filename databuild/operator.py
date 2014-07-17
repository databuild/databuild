import json
import yaml
import os

from databuild.compat import _open
from databuild.facets import sum_facets
from databuild.loader import load_classpath, load_classpath_whitelist


class Operator(object):
    operations = []

    def __init__(self, workbook, settings=None):
        self.workbook = workbook
        if settings is None:
            settings = workbook.settings
        self.settings = settings
        self.languages = self.build_languages()

        super(Operator, self).__init__()

    def build_languages(self):
        languages = {}
        for name, runtime in self.settings.LANGUAGES.items():
            RuntimeClass = load_classpath(runtime)
            languages[name] = RuntimeClass(self.workbook)
        return languages

    def apply_operations(self, build_files, echo=False):
        for build_file in build_files:
            operations = build_file.operations
            [self.apply_operation(op, build_file, echo) for op in operations]

    def apply_operation(self, operation, build_file, echo=False):
        if echo and operation['description']:
            print(operation['description'])

        if 'expression' in operation['params']:
            operation['params']['expression'] = self.parse_expression(operation['params']['expression'], build_file)

        if 'facets' in operation['params']:
            facets = [self.parse_expression(facet['expression'], build_file) for facet in operation['params']['facets']]
            operation['params']['facets'] = sum_facets(facets)

        kwargs = operation['params']
        context = {
            'workbook': self.workbook,
            'buildfile': build_file,
        }

        # Short-circuit if the adapter has an optimized operation method
        if hasattr(self.workbook, operation['operation'].replace('.', '_')):
            fn = getattr(self.workbook, operation['operation'].replace('.', '_'))
            fn(context, **kwargs)
        else:
            fn = load_classpath_whitelist(operation['operation'], self.settings.OPERATION_MODULES, shortcuts=True)
            fn(context, **kwargs)

        self.operations.append(operation)

    def parse_expression(self, expression, build_file=None):
        assert not (expression.get('content') and expression.get('path'))

        language = expression['language']

        filename = expression.get('path')
        if filename:
            if not os.path.exists(filename):
                relative_path = build_file.parent_dir
                filename = os.path.join(relative_path, filename)

            with _open(filename, 'r', encoding='utf-8') as fh:
                exp = fh.read()
        else:
            exp = expression['content']
        runtime = self.languages[language]
        return runtime.eval(exp)
