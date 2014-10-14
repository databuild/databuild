from copy import deepcopy
import os
import six

from databuild.compat import _open
from databuild.facets import sum_facets
from databuild.loader import load_classpath, load_classpath_whitelist
from databuild.utils import render_string, recursive_render


runtime_operations = {}
runtime_tasks = {}


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

    def apply_operations(self, build_files, *args, **kwargs):
        for build_file in build_files:
            operations = build_file.operations
            [self.apply_operation(op, build_file, *args, **kwargs) for op in operations]

    def apply_operation(self, operation, build_file, context=None, echo=False):
        if not operation.get('enabled', True):
            return

        if context is None:
            context = {}

        context.update({
            'workbook': self.workbook,
            'buildfile': build_file,
        })

        if 'context' in operation:
            context.update(operation['context'])

        operation_name = operation['operation']
        if operation_name in runtime_operations:
            operation_name, description, kwargs = runtime_operations[operation_name]
            kwargs.update(operation['params'])
        else:
            description = operation.get('description', '')
            kwargs = operation['params']

        if 'expression' in kwargs:
            backup_expression = deepcopy(kwargs['expression'])
            kwargs['expression'] = self.parse_expression(kwargs['expression'], build_file, context=context)

        if 'facets' in kwargs:
            backup_facets = deepcopy(kwargs['facets'])
            facets = [self.parse_expression(facet['expression'], build_file) for facet in kwargs['facets']]
            kwargs['facets'] = sum_facets(facets)

        # Short-circuit if the adapter has an optimized operation method
        if hasattr(self.workbook, operation_name.replace('.', '_')):
            fn = getattr(self.workbook, operation_name.replace('.', '_'))
        else:
            fn = load_classpath_whitelist(operation_name, self.settings.OPERATION_MODULES, shortcuts=True)

        if echo and description:
            _description = render_string(description, context)
            print(_description)

        for k, v in kwargs.items():
            kwargs[k] = recursive_render(v, context)

        fn(context, **kwargs)

        if 'expression' in kwargs:
            kwargs['expression'] = backup_expression
        if 'facets' in kwargs:
            kwargs['facets'] = backup_facets

        self.operations.append(operation)

    def parse_expression(self, expression, build_file=None, context=None):
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

        if context is None:
            context = {}

        runtime = self.languages[language]
        return runtime.eval(exp, context)
