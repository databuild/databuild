import os
import shutil
import subprocess

def call_command(context, command, arguments=None):
    if arguments is None:
        arguments = []
    call_args = [command] + arguments
    subprocess.check_call(call_args)


def remove_dir(context, path):
    if not path.startswith('/'):
        path = os.path.join(context['buildfile'].parent_dir, path)
    shutil.rmtree(path, ignore_errors=True)


def make_dir(context, path):
    if not path.startswith('/'):
        path = os.path.join(context['buildfile'].parent_dir, path)
    os.makedirs(path)
