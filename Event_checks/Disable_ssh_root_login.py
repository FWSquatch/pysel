from .Utils import Utils

def Disable_ssh_root_login():
    if Utils.string_exists('/etc/ssh/sshd_config', 'PermitRootLogin no'):
        return True
    else:
        return False