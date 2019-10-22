from .Utils import Utils
import os

def Secure_ssh(flaw):
    if os.path.exists('/etc/ssh/sshd_config'):
        if flaw == 'defaultPortChange':
            if Utils.string_exists('/etc/ssh/sshd_config', '^Port 22'):
                return False
            else:
                if not Utils.string_exists('/etc/ssh/sshd_config', '^Port'):
                    return False
                else:
                    return True
        elif flaw == 'PermitRootLoginNo':
            if Utils.string_exists('/etc/ssh/sshd_config', '^PermitRootLogin no'):
                return True
            else:
                return False
        elif flaw == 'Protocol2Only':
            if Utils.string_exists('/etc/ssh/sshd_config', '^Protocol 2,1') or Utils.string_exists('/etc/ssh/sshd_config', '^Protocol 1,2'):
                return False
            else:
                return True
        elif flaw == 'UsePAMyes':
            if Utils.string_exists('/etc/ssh/sshd_config', '^UsePAM no'):
                return False
            else:
                return True
        elif flaw == 'PermitUserEnvironmentNo':
            if Utils.string_exists('/etc/ssh/sshd_config', '^PermitUserEnvironment yes'):
                return False
            else:
                return True
        elif flaw == 'PermitEmptyPasswordsNo':
            if Utils.string_exists('/etc/ssh/sshd_config', '^PermitEmptyPasswords yes'):
                return False
            else:
                return True
    else:
        return False
