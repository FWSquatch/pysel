from .Utils import Utils

def Add_users(user):
    if Utils.string_exists('/etc/passwd', user):
        return True
    else:
        return False 