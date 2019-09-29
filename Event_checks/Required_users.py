from .Utils import Utils

def Required_users(user):
    if Utils.string_exists('/etc/passwd', user):
        return False
    else:
        return True    