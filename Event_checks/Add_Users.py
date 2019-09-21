from .Utils import Utils

def Add_Users(users):
    if len(users) > 1:
        return_val = False
        for user in users:
            if Utils.string_exists('passwd', user):
                return_val = True
            else:
                return_val = False
        return return_val
    else:
        if Utils.string_exists('passwd', users[0]):
            return True
    