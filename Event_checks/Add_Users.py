from .Utils import Utils

def Add_Users(user):
    if Utils.string_exists('/etc/passwd', user):
        return True
    else:
        return False 