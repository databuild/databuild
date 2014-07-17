import json
import os
import yaml

from cached_property import cached_property
from databuild.compat import _open


class BuildFile(object):
    def __init__(self, path):
        self.path = os.path.abspath(path)
        super(BuildFile, self).__init__()

    @property
    def parent_dir(self):
        return os.path.dirname(self.path)

    @cached_property
    def operations(self):
        with _open(self.path, 'r', encoding='utf-8') as fh:
            if self.path.endswith('.json'):
                operations = json.load(fh)
            elif self.path.endswith('.yaml') or self.path.endswith('.yml'):
                operations = yaml.safe_load(fh)
        return operations
