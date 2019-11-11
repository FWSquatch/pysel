from .Utils import Utils
## Settings taken from here: https://www.adamcouch.co.uk/linux-account-lockout-policy-using-pam-with-ubuntu-server/

import re
def Check_account_lockout(parameter_value):
    authfile = '/etc/pam.d/common-password'
    f = open(authfile, 'r')
 
    if ":" in parameter_value: ## Does our parameter also have a value (i.e. minlen:8)
        parameter, value = parameter_value.split(':')[0], int(parameter_value.split(':')[1])
        if parameter == 'Deny':
            searchString = '^\s*[^\s*#].*deny=([^\s]+)' ## Deny access if user excedes this value
            for line in f.readlines():
                if re.search(searchString, line):
                    length = re.findall('deny=([^\s]+)', line)
                    if int(length[0]) <= value:
                        return True
            return False

    if ":" in parameter_value: ## Does our parameter also have a value (i.e. minlen:8)
        parameter, value = parameter_value.split(':')[0], int(parameter_value.split(':')[1])
        if parameter == 'UnlockTime':
            searchString = '^\s*[^\s*#].*unlock_time=([^\s]+)' ## How many seconds to lock out the user after max login attempts
            for line in f.readlines():
                if re.search(searchString, line):
                    length = re.findall('unlock_time=([^\s]+)', line)
                    if int(length[0]) >= value:
                        return True
            return False

    if ":" in parameter_value: ## Does our parameter also have a value (i.e. minlen:8)
        parameter, value = parameter_value.split(':')[0], int(parameter_value.split(':')[1])
        if parameter == 'RootUnlockTime':
            searchString = '^\s*[^\s*#].*root_unlock_time=([^\s]+)' ## Lock out the root account for this many seconds after failed logins
            for line in f.readlines():
                if re.search(searchString, line):
                    length = re.findall('root_unlock_time=([^\s]+)', line)
                    if int(length[0]) >= value:
                        return True
            return False

    if parameter_value == 'OnErrorFail':
        searchString = '^\s*[^\s*#].*onerror=fail' ## Upon an error issue a fail
        if Utils.string_exists(authfile, searchString):
            return True
        else:
            return False
    elif parameter_value == 'Audit':
        searchString = '^\s*[^\s*#].*audit'  ## Will log the username into syslog if the user is not found
        if Utils.string_exists(authfile, searchString):
            return True
        else:
            return False
    elif parameter_value == 'EvenDenyRoot':
        searchString = '^\s*[^\s*#].*even_deny_root'  ## Will log the username into syslog if the user is not found
        if Utils.string_exists(authfile, searchString):
            return True
        else:
            return False
    else:
        print('O LAWWWRD!')
        return False