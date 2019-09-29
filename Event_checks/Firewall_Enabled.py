from .Utils import Utils

def Firewall_Enabled(null):
    if Utils.run_command('sudo /usr/sbin/ufw status') == b'Status: active\n':
        return True
    else:
        return False