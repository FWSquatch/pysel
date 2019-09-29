from .Utils import Utils

def Perm_now_equal_to(file_perm):
    data = file_perm.split(':')
    if Utils.check_perm(data[0]) == data[1]:
        return True
    else:
        return False  