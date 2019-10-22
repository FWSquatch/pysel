from .Utils import Utils

def Package_updated_to_version(package_version):
    package, version = package_version.split(':')[0], package_version.split(':')[1]
    command = 'apt-cache policy ' + package
    output = Utils.run_command(command).decode().splitlines()
    installed = output[1]
    if installed.split()[1] == version:
        return True
    else:
        return False

