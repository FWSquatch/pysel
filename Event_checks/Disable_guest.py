from .Utils import Utils
def Disable_guest():
    if Utils.string_exists('/etc/os-release', 'VERSION_ID="14.04"') or Utils.string_exists('/etc/os-release', 'VERSION_ID="16.04"'):
        if Utils.string_exists('/etc/lightdm/lightdm.conf','allow-guest=true') or Utils.string_exists('/etc/lightdm.conf.d/*', 'allow-guest=true'):
            return False
        else:
            return True 
    else:
        # Must be 18.04 - Do we need a guest check?
        return True