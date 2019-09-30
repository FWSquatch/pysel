from .Utils import Utils

def Bad_file(filename):
    if Utils.file_exists(filename):
        return False
    else:
        return True