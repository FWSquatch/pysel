#!/usr/bin/env python3

import subprocess

def run_command(command):
    command = command.split(' ')
    cmd = subprocess.Popen(command, stdout=subprocess.PIPE)
    return cmd.stdout.read()


def service_running(service):
    command = 'sudo systemctl status ' + service
    output = str(run_command(command))
    if 'active' in output:
        return True
    else:
        return False

print(service_running('mosquitto'))