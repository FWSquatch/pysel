from .Utils import Utils

def Remove_from_sudo(user):
    if Utils.user_in_group('sudo', user):
        return False
    else:
        return True   