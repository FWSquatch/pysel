from .Utils import Utils

## Sources: https://github.com/virtadpt/ubuntu-hardening/blob/master/16.04-lts/login.defs 

def Secure_login_defs(flaw):
    if flaw == 'PasswordMaxDays':
        if Utils.string_exists('/etc/login.defs', '^PASS_MAX_DAYS\s*99999'):
            return False
        else:
            return True
    elif flaw == 'PasswordMinDays':
        if Utils.string_exists('/etc/login.defs', '^PASS_MIN_DAYS\s*0'):
            return False
        else:
            return True
    elif flaw == 'PasswordWarnAge':
        if Utils.string_exists('/etc/login.defs', '^PASS_MIN_AGE\s*7'):
            return False
        else:
            return True
    elif flaw == 'LogUnknownFail':
        if Utils.string_exists('/etc/login.defs', '^LOG_UNKFAIL_ENAB\s*yes'):
            return True
        else:
            return False
    elif flaw == 'LogOkLogins':
        if Utils.string_exists('/etc/login.defs', '^LOG_OK_LOGINS\s*yes'):
            return True
        else:
            return False
    elif flaw == 'SuLogFile':
        if Utils.string_exists('/etc/login.defs', '^SULOG_FILE'):
            return True
        else:
            return False
