from .Utils import Utils

def Prohibited_packages(package):
    if Utils.package_installed(package):
        return False
    else:
        return  True