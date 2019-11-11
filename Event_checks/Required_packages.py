from .Utils import Utils

def Required_packages(package):
    if Utils.package_installed(package):
        return True
    else:
        return False