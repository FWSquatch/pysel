from .Utils import Utils

def Weak_password(userName):
    strongPass = userName + ":$"
    print('strongPass:', strongPass)
    if Utils.string_exists('/etc/shadow',strongPass):
        return True
    else:
        return False