from .Utils import Utils

def Firewall_rule_exists(portNumber):
    result = Utils.run_command("ufw status").decode().rstrip()
    if portNumber in result:
        return True
    else:
        return False
