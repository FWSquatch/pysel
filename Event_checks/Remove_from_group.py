from .Utils import Utils

def Remove_from_group(user_group):
    data = user_group.split(':')
    if Utils.user_in_group(data[0], data[1]):
        return False
    else:
        return True   