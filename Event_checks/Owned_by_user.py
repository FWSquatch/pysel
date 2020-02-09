from .Utils import Utils

def Owned_by_user(setting):
    data = setting.split(':',1)
    filename = data[0]
    user = data[1]
    command = 'ls -l ' + str(filename)
    result = (Utils.run_command(command).decode()).split(' ')[2]
    if result == user:
        return True
    else:
        return False
