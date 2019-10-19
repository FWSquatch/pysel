from .Utils import Utils

def Package_updated_latest(package):
    command = 'apt-cache policy ' + package
    output = Utils.run_command(command).decode().splitlines()
    installed, candidate = output[1] , output[2]
    if installed.split()[1] == candidate.split()[1]:
        return True
    else:
        return False


