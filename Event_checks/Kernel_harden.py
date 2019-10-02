from Utils import Utils

def Kernel_harden(parameter_value):
    if parameter_value == 'BlockModLoading':
        ## check /proc/sys/kernel/modules_disabled to contain 1 - Blocks the loading of kernel modules
    elif parameter_value == 'DmesgRestrict':
        ## check /proc/sys/kernel/dmesg_restrict to contain 1 - Block output of dmesg
    elif parameter_value == 'KexecLoadDisabled':
        ## check /proc/sys/kernel/kexec_load_disabled to contain 1 Block loading alternate kernels
    