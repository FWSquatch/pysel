from .Utils import Utils

def Check_user_password(user_parameter):
    user,check = user_parameter.split(':')[0], user_parameter.split(':')[1]
    command = 'passwd -S ' + user
    pwReport = (Utils.run_command(command)).decode().split()
    if Utils.string_exists('/etc/passwd', user):
      if check == 'NoPassword':  ## User now has a password
        if pwReport[1] == 'NP':
            return False 
        else:
            return True

      elif check == 'MinDays': ## User now has a minimum password age
        if int(pwReport[3]) == 0:
            return False
        else:
            return True    
      elif check == 'MaxDays': ## User now has a maximum password age
        if int(pwReport[4]) <= 60:
            return True
        else:
            return False
    else:
        return False
