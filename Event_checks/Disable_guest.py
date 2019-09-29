from .Utils import Utils

def Disable_guest(null):
    #if Utils.string_exists('/etc/lsb-release', 'DISTRIB_RELEASE=18.04'):
    #    return True
    if Utils.string_exists('/etc/lightdm/lightdm.conf','allow-guest=false'):
        return True
    elif Utils.string_exists('/etc/lightdm.conf.d/*', 'allow-guest=false'):
        return True
    else:
        return False 