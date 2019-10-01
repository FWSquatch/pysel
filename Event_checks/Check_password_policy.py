from Utils import Utils
## Settings taken from here: https://computingforgeeks.com/enforce-strong-user-password-policy-ubuntu-debian/
import re
def Check_password_policy(parameter_value):
    '''
    if ":" in parameter_value: ## Does our parameter also have a value (i.e. minlen:8)
        parameter, lenValue = parameter_value.split(':')[0], int(parameter_value.split(':')[1])
        f = open('common-password', 'r')    
        if parameter == 'MinLen':
            searchString = '^\s*[^\s*#].*minlen=([^\s]+)' ## Find uncommented lines with minlen= in them
            for line in f.readlines():
                return_value = False
                if re.search(searchString, line):
                #if re.search('minlen=([^\s]+)', line):
                    length = re.search('minlen=([^\s]+)', line)
                    if int(length[1]) >=lenValue:
                        return_value = True
                    else:
                        return_value = False
                else:
                    return_value = False
                return return_value

        elif parameter == 'Retry':
            searchString = '^\s*[^\s*#].*retry=([^\s]+)' ## Find uncommented lines with retry= in them
            for line in f.readlines():
                print(line)
                return_value = False
                if re.search(searchString, line):
                    retry = re.search('retry=([^\s]+)', line)
                    print(retry[1])
                    if int(retry[1]) <=lenValue:
                        return_value = True
                    else:
                        return_value = False
                else:
                    print('wtf')
                    return_value = False
                return return_value
    else: ## They passed us a single parameter
    '''
    if parameter_value == 'RejectUsername':
        searchString = '^\s*[^\s*#].*reject_username' ## Do not use name of user in straight or reversed form
        if Utils.string_exists('common-password', searchString):
            return True
        else:
            return False
    elif parameter_value == 'EnforceForRoot':
        searchString = '^\s*[^\s*#].*enforce_for_root'  ## Enforce policy for root user
        if Utils.string_exists('common-password', searchString):
            return True
        else:
            return False


print(Check_password_policy('RejectUsername'))