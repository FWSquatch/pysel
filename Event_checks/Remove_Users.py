from .Utils import Utils

def Remove_Users(users):
    if len(users) > 1:
        return_val = False
        for user in users:
            ## If the user still exists in the file then set the return value to false
            if Utils.string_exists('/etc/passwd', user):
                return_val = False
            else:
                return_val = True
        return return_val
    else:
        if Utils.string_exists('/etc/passwd', users[0]):
            return False