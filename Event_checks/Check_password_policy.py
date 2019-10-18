from .Utils import Utils
## Settings taken from here: https://computingforgeeks.com/enforce-strong-user-password-policy-ubuntu-debian/

import re
def Check_password_policy(parameter_value):
    pwfile = '/etc/pam.d/common-password'
    authfile = '/etc/pam.d/common-auth'
    f = open(pwfile, 'r')
    g = open(authfile, 'r')
    if ":" in parameter_value: ## Does our parameter also have a value (i.e. minlen:8)
        parameter, value = parameter_value.split(':')[0], int(parameter_value.split(':')[1])
        if parameter == 'MinLen':
            searchString = '^\s*[^\s*#].*minlen=([^\s]+)' ## Find uncommented lines with minlen= in them
            for line in f.readlines():
                if re.search(searchString, line):
                    length = re.findall('minlen=([^\s]+)', line)
                    if int(length[0]) >= value:
                        return True
            return False

    if ":" in parameter_value: ## Does our parameter also have a value (i.e. minlen:8)
        parameter, value = parameter_value.split(':')[0], int(parameter_value.split(':')[1])
        if parameter == 'Retry':
            searchString = '^\s*[^\s*#].*retry=([^\s]+)' ## Find uncommented lines with retry= in them
            for line in f.readlines():
                if re.search(searchString, line):
                    checkValue = re.findall('retry=([^\s]+)', line)
                    if int(checkValue[0]) <= value:
                        return True
            return False    

    if ":" in parameter_value: ## Does our parameter also have a value (i.e. minlen:8)
        parameter, value = parameter_value.split(':')[0], int(parameter_value.split(':')[1])
        if parameter == 'MaxRepeat':
            searchString = '^\s*[^\s*#].*maxrepeat=([^\s]+)' ## Allow a maximum of n repeated characters
            for line in f.readlines():
                if re.search(searchString, line):
                    checkValue = re.findall('maxrepeat=([^\s]+)', line)
                    if int(checkValue[0]) >= value:
                        return True
            return False    

    if ":" in parameter_value: ## Does our parameter also have a value (i.e. minlen:8)
        parameter, value = parameter_value.split(':')[0], int(parameter_value.split(':')[1])
        if parameter == 'UCredit':
            searchString = '^\s*[^\s*#].*ucredit=([^\s]+)' ## Number of uppercase to have in password
            for line in f.readlines():
                if re.search(searchString, line):
                    checkValue = re.findall('ucredit=([^\s]+)', line)
                    if int(checkValue[0]) >= value:
                        return True
            return False    

    if ":" in parameter_value: ## Does our parameter also have a value (i.e. minlen:8)
        parameter, value = parameter_value.split(':')[0], int(parameter_value.split(':')[1])
        if parameter == 'LCredit':
            searchString = '^\s*[^\s*#].*lcredit=([^\s]+)' ## Number of lowercase to have in password
            for line in f.readlines():
                if re.search(searchString, line):
                    checkValue = re.findall('lcredit=([^\s]+)', line)
                    if int(checkValue[0]) >= value:
                        return True
            return False    

    if ":" in parameter_value: ## Does our parameter also have a value (i.e. minlen:8)
        parameter, value = parameter_value.split(':')[0], int(parameter_value.split(':')[1])
        if parameter == 'DCredit':
            searchString = '^\s*[^\s*#].*dcredit=([^\s]+)' ## Number of digits to have in password
            for line in f.readlines():
                if re.search(searchString, line):
                    checkValue = re.findall('dcredit=([^\s]+)', line)
                    if int(checkValue[0]) >= value:
                        return True
            return False    

    if ":" in parameter_value: ## Does our parameter also have a value (i.e. minlen:8)
        parameter, value = parameter_value.split(':')[0], int(parameter_value.split(':')[1])
        if parameter == 'DifOk':
            searchString = '^\s*[^\s*#].*difok=([^\s]+)' ## The number of characters in new password that must not exist in old password
            for line in f.readlines():
                if re.search(searchString, line):
                    checkValue = re.findall('difok=([^\s]+)', line)
                    if int(checkValue[0]) >= value:
                        return True
            return False    

    if ":" in parameter_value: ## Does our parameter also have a value (i.e. minlen:8)
        parameter, value = parameter_value.split(':')[0], int(parameter_value.split(':')[1])
        if parameter == 'GecosCheck':
            searchString = '^\s*[^\s*#].*gecoscheck=([^\s]+)' ## Do not use words in the gecos field of passwd
            for line in f.readlines():
                if re.search(searchString, line):
                    checkValue = re.findall('gecoscheck=([^\s]+)', line)
                    if int(checkValue[0]) == value:  ##  Should really only be set to 1 or 0
                        return True
            return False    

    if ":" in parameter_value: ## Does our parameter also have a value (i.e. minlen:8)
        parameter, value = parameter_value.split(':')[0], int(parameter_value.split(':')[1])
        if parameter == 'LockoutTally':
            searchString = '(?i)^\s*auth[^\n]*pam_tally2.so[^\n]*deny=[0-9]+' ## Do not use words in the gecos field of passwd
            for line in g.readlines():
                if re.search(searchString, line):
                    return True
            return False  

    if ":" in parameter_value: ## Does our parameter also have a value (i.e. minlen:8)
        parameter, value = parameter_value.split(':')[0], int(parameter_value.split(':')[1])
        if parameter == 'Remember':
            searchString = '^\s*[^\s*#].*remember=([^\s]+)' ## How many passwords to remember
            for line in f.readlines():
                if re.search(searchString, line):
                    checkValue = re.findall('remember=([^\s]+)', line)
                    if int(checkValue[0]) >= value:  
                        return True
            return False  

    if parameter_value == 'RejectUsername':
        searchString = '^\s*[^\s*#].*reject_username' ## Do not use name of user in straight or reversed form
        if Utils.string_exists(pwfile, searchString):
            return True
        else:
            return False
    elif parameter_value == 'EnforceForRoot':
        searchString = '^\s*[^\s*#].*enforce_for_root'  ## Enforce policy for root user
        if Utils.string_exists(pwfile, searchString):
            return True
        else:
            return False