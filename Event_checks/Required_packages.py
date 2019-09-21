from .Utils import Utils
def Required_packages(packages):
    if len(packages) > 1:
        return_val = False
        for package in packages:
            if Utils.package_installed(package):
                return_val = True
            else:
                return_val = False
        return return_val
    else:
        if Utils.package_installed(packages[0]):
            return True
        else:
            return False