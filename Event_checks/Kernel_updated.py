from .Utils import Utils

def Kernel_updated(initialVersion):
    if Utils.check_kernel() != str(initialVersion):
        return True
    else:
        return False