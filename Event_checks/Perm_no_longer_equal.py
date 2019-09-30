from .Utils import Utils

def Perm_no_longer_equal(file_perm):
    data = file_perm.split(':')
    if Utils.check_perm(data[0]) != data[1]:
        return True
    else:
        return False  