import subprocess

def call_command(context, command, arguments=None):
    if arguments is None:
        arguments = []
    call_args = [command] + arguments
    subprocess.check_call(call_args)
