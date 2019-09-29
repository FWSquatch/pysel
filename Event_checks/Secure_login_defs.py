from .Utils import Utils

def Secure_login_defs(flaw):
    if flaw == 'PasswordMaxDays':
        if Utils.string_exists('/etc/login.defs', '^PASS_MAX_DAYS\t99999'):
            return False
        else:
            return True
    elif flaw == 'PasswordMinDays':
        if Utils.string_exists('/etc/login.defs', '^PASS_MIN_DAYS\t0'):
            return False
        else:
            return True
    elif flaw == 'PasswordWarnAge':
        if Utils.string_exists('/etc/login.defs', '^PASS_MIN_AGE\t7'):
            return False
        else:
            return True
    elif flaw == 'LogUnknownFail':
        if Utils.string_exists('/etc/login.defs', '^LOG_UNKFAIL_ENAB\tno'):
            return False
        else:
            return True
    elif flaw == 'LogOkLogins':
        if Utils.string_exists('/etc/login.defs', '^LOG_OK_LOGINS\tno'):
            return False
        else:
            return True
    elif flaw == 'SuLogFile':
        if Utils.string_exists('/etc/login.defs', '^SULOG_FILE'):
            return False
        else:
            return True