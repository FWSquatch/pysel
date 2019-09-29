from .Utils import Utils

def Required_Users(user):
    if Utils.string_exists('/etc/passwd', user):
        return False
    else:
        return True    