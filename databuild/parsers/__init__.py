from databuild.loader import load_classpath


def parse_expression(expression, wrap=True):
    language, exp = expression['language'], expression['content']
    parse = load_classpath(language)
    return parse(exp, wrap)
