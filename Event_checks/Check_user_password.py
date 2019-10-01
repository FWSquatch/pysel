from .Utils import Utils

def Check_user_password(user_parameter):
    user,check = user_parameter.split(':')[0], user_parameter.split(':')[1]

    if check == 'NoPassword':  ## User now has a password
        command = 'passwd -S ' + user
        pwReport = (Utils.run_command(command)).decode().split()
        if pwReport[1] == 'NP':
            return False
        else:
            return True

    elif check == 'MinDays': ## User now has a minimum password age
        searchString = '^' + user + '\:([^\:]*\:){2}[^0]' ## User no longer has 0 in the min age position
        if Utils.string_exists('/etc/shadow', searchString):
            return False
        else:
            return True    
    elif check == 'MaxDays': ## User now has a maximum password age
        searchString = '^' + user + '\:([^\:]*\:){3}9{5}' ## User no longer has 99999 in max age position
        if Utils.string_exists('/etc/shadow', searchString):
            return False
        else:
            return True