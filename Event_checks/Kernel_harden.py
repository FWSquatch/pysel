from .Utils import Utils

## Sources: https://github.com/xairy/ubuntu-hardening
##          https://wiki.ubuntu.com/Security/Features
##          https://blog.aquasec.com/ebpf-vulnerability-cve-2017-16995-when-the-doorman-becomes-the-backdoor
## Sources: https://www.sysadmin.md/hardening-existing-linux-server-via-sysctl-parameters.html
##          https://security.stackexchange.com/questions/209529/what-does-enabling-kernel-unprivileged-userns-clone-do 

def Kernel_harden(parameter_value):
  if parameter_value == 'BlockModLoading': ## Blocks the loading of kernel modules
    if Utils.string_exists('/proc/sys/kernel/modules_disabled', '1'):
      return True
  elif parameter_value == 'DmesgRestrict': ## Block output of dmesg
    if Utils.string_exists('/proc/sys/kernel/dmesg_restrict', '1'):
      return True
  elif parameter_value == 'KexecLoadDisabled': ## Block loading alternate kernels
    if Utils.string_exists('/proc/sys/kernel/kexec_load_disabled', '1'):
      return True
  elif parameter_value == 'UnprivBpfDisabled': ## Disable Unprivileged BPF (packet filtering)
    if Utils.string_exists('/proc/sys/kernel/unprivileged_bpf_disabled', '1'):
      return True
  elif parameter_value == 'CoreUsesPid':
    if Utils.string_exists('/proc/sys/kernel/core_uses_pid', '1'):
      return True
  elif parameter_value == 'CtrlAltDel':
    if Utils.string_exists('/proc/sys/kernel/ctrl-alt-del','0'):
      return True
  elif parameter_value == 'SysRq':
    if Utils.string_exists('/proc/sys/kernel/sysrq','0'):
      return True
  elif parameter_value == 'AllRejectAcceptRedirects': ## This is not a router, so don't redirect
    if Utils.string_exists('/proc/sys/net/ipv4/conf/all/accept_redirects','0'):
      return True
  elif parameter_value == 'DefRejectAcceptRedirects': ## This is not a router, so don't redirect
    if Utils.string_exists('/proc/sys/net/ipv4/conf/default/accept_redirects','0'):
      return True
  elif parameter_value == 'AllDisableAcceptSourceRoute': ## Source routed packets can allow packets through untrusted interfaces
    if Utils.string_exists('/proc/sys/net/ipv4/conf/all/accept_source_route','0'):
      return True
  elif parameter_value == 'DefDisableAcceptSourceRoute': ## Source routed packets can allow packets through untrusted interfaces
    if Utils.string_exists('/proc/sys/net/ipv4/conf/default/accept_source_route','0'):
      return True
  elif parameter_value == 'BootPReplay':
    if Utils.string_exists('/proc/sys/net/ipv4/conf/all/bootp_relay','0'):
      return True
  elif parameter_value == 'Ipv4Forwarding':
    if Utils.string_exists('/proc/sys/net/ipv4/conf/all/forwarding','0'):
      return True
  elif parameter_value == 'AllLogMartians':
    if Utils.string_exists('/proc/sys/net/ipv4/conf/all/log_martians','0'): ## Log packets from impossible (martian) ip addresses
      return True
  elif parameter_value == 'DefLogMartians':
    if Utils.string_exists('/proc/sys/net/ipv4/conf/default/log_martians','0'): ## Log packets from impossible (martian) ip addresses
       return True
  elif parameter_value == 'McForwarding':
    if Utils.string_exists('/proc/sys/net/ipv4/conf/all/mc_forwarding','0'):
       return True
  elif parameter_value == 'ProxyArp':
    if Utils.string_exists('/proc/sys/net/ipv4/conf/all/proxy_arp','0'):
      return True
  elif parameter_value == 'RpFilter': ## Helps prevent IP spoofing attacks
    if Utils.string_exists('/proc/sys/net/ipv4/conf/all/rp_filter','1'):
      return True
  elif parameter_value == 'DisableSendRedirects': ## Only routers would do this. We are not a router
    if Utils.string_exists('/proc/sys/net/ipv4/conf/all/send_redirects','0'):
      return True
  elif parameter_value == 'IgnoreIcmpBroadcast': ## Prevent Smurf attacks
    if Utils.string_exists('/proc/sys/net/ipv4/icmp_echo_ignore_broadcast','1'):
      return True
  elif parameter_value == 'IgnoreIcmpBogusError':
    if Utils.string_exists('/proc/sys/net/ipv4/icmp_ignore_bogus_error_responses','1'):
      return True
  elif parameter_value == 'TcpSynCookies': ## Prevent SYN flood DDoS attacks
    if Utils.string_exists('/proc/sys/net/ipv4/tcp_syncookies','1'):
      return True
  elif parameter_value == 'TcpTimestamps':
    if Utils.string_exists('/proc/sys/net/ipv4/tcp_timestamps','0'):
      return True    
  elif parameter_value == 'DisableUnprivUserNameSpace': ## Disable unprivilged user namespaces. Reduces attack surface of he kernel
    if Utils.string_exists('/proc/sys/kernel/unprivileged_userns_clone','1'):
      return True
  else:
    return False