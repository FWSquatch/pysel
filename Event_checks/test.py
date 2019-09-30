from Utils import Utils

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
    elif flaw == 'DisableIcmpRedirects': ## This is not a router, so don't redirect
        if Utils.string_exists('/etc/sysctl.conf', '^net.ipv4.conf.all.accept_redirects.*=.*0'):
            return True
        else:
            return False
    elif flaw == 'DisableSourceRoutedPackets': ## Source routed packets can allow packets through untrusted interfaces
        if Utils.string_exists('/etc/sysctl.conf', '^net.ipv4.conf.all.accept_source_route.*=.*0'):
            return True
        else:
            return False


print(Secure_sysctl('DisableSourceRoutedPackets'))