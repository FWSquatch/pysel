from .Utils import Utils

def Firewall_enabled(null):
    result = Utils.run_command('sudo /usr/sbin/ufw status').decode().split('\n')
    print(result[0])
    if result[0] == 'Status: active':
#    if Utils.run_command('sudo /usr/sbin/ufw status') == b'Status: active\n':
        return True
    else:
        return False
