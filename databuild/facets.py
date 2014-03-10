from databuild.functional import compose


def sum_facets(facets):
    if len(facets) == 0:
        return None
    return compose(*facets)
