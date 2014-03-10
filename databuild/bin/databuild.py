#!/usr/bin/env python

import json

from databuild import settings
from databuild.loader import load_classpath

AdapterClass = load_classpath(settings.ADAPTER) 

def main(build_file, **kwargs):
    book = AdapterClass()
    operations = json.load(build_file)
    book.apply_operations(operations)
