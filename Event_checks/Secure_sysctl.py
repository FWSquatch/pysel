from .Utils import Utils

#### THIS MODULE HAS BEEN FOLDED INTO Kernel_harden.py ####


## Sources: https://www.sysadmin.md/hardening-existing-linux-server-via-sysctl-parameters.html
##          https://security.stackexchange.com/questions/209529/what-does-enabling-kernel-unprivileged-userns-clone-do 

def Secure_sysctl(flaw):
    if flaw == 'TcpSynFloodProtection': 
        if Utils.string_exists('/etc/sysctl.conf', '^net.ipv4.tcp_syncookies=.*1'):
            return True
        else:
            return False
    elif flaw == 'IgnoreIcmpBroadcasts': 
        if Utils.string_exists('/etc/sysctl.conf', '^net.ipv4.icmp_echo_ignore_broadcasts.*=.*1'):
            return True
        else:
            return False
    elif flaw == 'RejectIcmpRedirects': 
        if Utils.string_exists('/etc/sysctl.conf', '^net.ipv4.conf.all.accept_redirects.*=.*0'):
            return True
        else:
            return False
    elif flaw == 'DisableSourceRoutedPackets': 
        if Utils.string_exists('/etc/sysctl.conf', '^net.ipv4.conf.all.accept_source_route.*=.*0'):
            return True
        else:
            return False
    elif flaw == 'EnableReversePathFiltering': 
        if Utils.string_exists('/etc/sysctl.conf', '^net.ipv4.conf.all.rp_filter.*=.*1'):
            return True
        else:
            return False
    elif flaw == 'LogMartianPackets': 
        if Utils.string_exists('/etc/sysctl.conf', '^net.ipv4.conf.all.log_martians.*=.*1'):
            return True
        else:
            return False    
    elif flaw == 'DisableSendIcmpRedirects': 
        if Utils.string_exists('/etc/sysctl.conf', '^net.ipv4.conf.all.send_redirects.*=.*0'):
            return True
        else:
            return False  
    elif flaw == 'DisableUnprivilgedUserNs': 
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