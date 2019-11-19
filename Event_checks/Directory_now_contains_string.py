from .Utils import Utils

def Directory_now_contains_string(setting):
    data = setting.split(':',1)
    directory = data[0]
    string = data[1]
    if Utils.string_exists_in_dir(directory, string):
        return True
    else:
        return False

