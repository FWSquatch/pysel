from .Utils import Utils

## Sources: https://github.com/xairy/ubuntu-hardening
##          https://wiki.ubuntu.com/Security/Features
##          https://blog.aquasec.com/ebpf-vulnerability-cve-2017-16995-when-the-doorman-becomes-the-backdoor


def Kernel_harden(parameter_value):
    if parameter_value == 'BlockModLoading':
        if Utils.string_exists('/proc/sys/kernel/modules_disabled', 1):
            return True
        ## check /proc/sys/kernel/modules_disabled to contain 1 - Blocks the loading of kernel modules
    elif parameter_value == 'DmesgRestrict':
        if Utils.string_exists('/proc/sys/kernel/dmesg_restrict', 1):
            return True
        ## check /proc/sys/kernel/dmesg_restrict to contain 1 - Block output of dmesg
    elif parameter_value == 'KexecLoadDisabled':
        if Utils.string_exists('/proc/sys/kernel/kexec_load_disabled', 1):
            return True
        ## check /proc/sys/kernel/kexec_load_disabled to contain 1 Block loading alternate kernels
    elif parameter_value == 'UnprivBpfDisabled':
        if Utils.string_exists('/proc/sys/kernel/unprivileged_bpf_disabled', 1):
            return True
        ## check /proc/sys/kernel/unprivileged_bpf_disabled to contain 1 - Disable Unprivileged BPF (packet filtering)
    else:
        return False