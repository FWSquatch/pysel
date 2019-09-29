from .Utils import Utils

def Remove_Users(user):
    if Utils.string_exists('/etc/passwd', user):
        return False
    else:
        return True        