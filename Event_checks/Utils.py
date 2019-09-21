import re
import subprocess

class Utils:

    @staticmethod
    def string_exists(targetFile, searchString):
        try:
            for line in open(targetFile, 'r').readlines():
                if re.search(searchString, line):
                    return True
            return False
        except FileExistsError:
            return False
    
    @staticmethod
    def run_command(command):
        command = command.split(' ')
        cmd = subprocess.Popen(command, stdout=subprocess.PIPE)
        return cmd.stdout.read()

    @staticmethod
    def package_installed(package):
        if package in Utils.run_command('dpkg --list'):
            return True
        else:
            return False
