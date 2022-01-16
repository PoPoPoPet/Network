import platform
import subprocess


def ping(host):
    param = '-n' if platform.system().lower() == 'windows' else '-c'

    command = ['ping', param, '4', host]
    return subprocess.call(command) == 0

ping('8.8.8.8')