from .Utils import Utils

def Prohibited_packages(packages):
    if len(packages) > 1:
        return_val = False
        for package in packages:
            if Utils.package_installed(package):
                return_val = False
            else:
                return_val = True
        return return_val
    else:
        if Utils.package_installed(packages[0]):
            return False
        else:
            return True