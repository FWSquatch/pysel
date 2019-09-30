from .Utils import Utils

def Add_to_sudo(user):
    if Utils.user_in_group('sudo', user):
        return True
    else:
        return False   