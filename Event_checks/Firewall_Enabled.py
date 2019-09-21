from .Utils import Utils

def Firewall_Enabled():
    if Utils.run_command('sudo /usr/sbin/ufw status') == b'Statuc: active\n':
        return True
    else:
        return False