from .Utils import Utils

## Used this guide to decide how/what to score:
## https://www.sysadmin.md/hardening-existing-linux-server-via-sysctl-parameters.html

def Secure_sysctl(flaw):
    if flaw == 'TcpSynFloodProtection': ## Prevent SYN flood DDoS attacks
        if Utils.string_exists('/etc/sysctl.conf', '^net.ipv4.tcp_syncookies=.*1'):
            return True
        else:
            return False
    elif flaw == 'IgnoreIcmpBroadcasts': ## Prevent Smurf attacks
        if Utils.string_exists('/etc/sysctl.conf', '^net.ipv4.icmp_echo_ignore_broadcasts.*=.*1'):
            return True
        else:
            return False
    elif flaw == 'RejectIcmpRedirects': ## This is not a router, so don't redirect
        if Utils.string_exists('/etc/sysctl.conf', '^net.ipv4.conf.all.accept_redirects.*=.*0'):
            return True
        else:
            return False
    elif flaw == 'DisableSourceRoutedPackets': ## Source routed packets can allow packets through untrusted interfaces
        if Utils.string_exists('/etc/sysctl.conf', '^net.ipv4.conf.all.accept_source_route.*=.*0'):
            return True
        else:
            return False
    elif flaw == 'EnableReversePathFiltering': ## Source routed packets can allow packets through untrusted interfaces
        if Utils.string_exists('/etc/sysctl.conf', '^net.ipv4.conf.all.rp_filter.*=.*1'):
            return True
        else:
            return False
    elif flaw == 'LogMartianPackets': ## Log packets from impossible (martian) ip addresses
        if Utils.string_exists('/etc/sysctl.conf', '^net.ipv4.conf.all.log_martians.*=.*1'):
            return True
        else:
            return False    
    elif flaw == 'DisableSendIcmpRedirects': ## Only routers would do this. We are not a router
        if Utils.string_exists('/etc/sysctl.conf', '^net.ipv4.conf.all.send_redirects.*=.*0'):
            return True
        else:
            return False  