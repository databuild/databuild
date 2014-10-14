import subprocess


def call_command(context, command, arguments):
    call_args = [command] + arguments
    subprocess.check_call(call_args)
