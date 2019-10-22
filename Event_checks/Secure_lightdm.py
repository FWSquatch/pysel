from .Utils import Utils

def Secure_lightdm(parameter):
    state = False
    # Look in /etc/lightdm, then look in all files in lightdm.conf.d (in order) return the last state found
    payload = '/etc/lightdm/|/etc/lightdm/lightdm.conf.d/:' + parameter
    if parameter == 'allow-guest':
        if Utils.conf_d_check(payload): ## This should be False
            state = False
        else:
            state = True
        return state
    elif parameter == 'greeter-hide-users': ## This should be True
        if Utils.conf_d_check(payload):
            state = True
        else:
            state = False
        return state    
    elif parameter == 'greeter-show-manual-login':## This should be True
        if Utils.conf_d_check(payload):
            state = True
        else:
            state = False
        return state    

