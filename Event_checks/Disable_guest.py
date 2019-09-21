from .Utils import Utils
def Disable_guest():
    if Utils.string_exists('/etc/lightdm/lightdm.conf','allow-guest=true'):
        return False
    else:
        return True 