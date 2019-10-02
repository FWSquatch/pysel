from .Utils import Utils

## Sources: https://www.sysadmin.md/hardening-existing-linux-server-via-sysctl-parameters.html
##          https://security.stackexchange.com/questions/209529/what-does-enabling-kernel-unprivileged-userns-clone-do 

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
    elif flaw == 'EnableReversePathFiltering': ## Helps prevent IP spoofing attacks
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
    elif flaw == 'DisableUnprivilgedUserNs': ## Disable unprivilged user namespaces. Reduces attack surface of he kernel
        if Utils.string_exists('/etc/sysctl.conf', '^kernel.unprivileged_userns_clone.*=.*1'):
            return True
        else:
            return False

'''
  Possible improvements:
  - Comparing sysctl key pairs with scan profile
    - kernel.core_uses_pid (exp: 1)                           
    - kernel.ctrl-alt-del (exp: 0)                            
    - kernel.kptr_restrict (exp: 1)                           
    - kernel.sysrq (exp: 0)                                   
    - net.ipv4.conf.all.accept_redirects (exp: 0)             
    - net.ipv4.conf.all.accept_source_route (exp: 0)          
    - net.ipv4.conf.all.bootp_relay (exp: 0)                  
    - net.ipv4.conf.all.forwarding (exp: 0)                   
    - net.ipv4.conf.all.log_martians (exp: 1)                 
    - net.ipv4.conf.all.mc_forwarding (exp: 0)                
    - net.ipv4.conf.all.proxy_arp (exp: 0)                    
    - net.ipv4.conf.all.rp_filter (exp: 1)                    
    - net.ipv4.conf.all.send_redirects (exp: 0)               
    - net.ipv4.conf.default.accept_redirects (exp: 0)         
    - net.ipv4.conf.default.accept_source_route (exp: 0)      
    - net.ipv4.conf.default.log_martians (exp: 1)             
    - net.ipv4.icmp_echo_ignore_broadcasts (exp: 1)           
    - net.ipv4.icmp_ignore_bogus_error_responses (exp: 1)     
    - net.ipv4.tcp_syncookies (exp: 1)                        
    - net.ipv4.tcp_timestamps (exp: 0)                        
    - net.ipv6.conf.all.accept_redirects (exp: 0)             
    - net.ipv6.conf.all.accept_source_route (exp: 0)          
    - net.ipv6.conf.default.accept_redirects (exp: 0)         
    - net.ipv6.conf.default.accept_source_route (exp: 0)      

'''