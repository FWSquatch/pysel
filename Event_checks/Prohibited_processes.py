from .Utils import Utils

def Prohibited_processes(process): # The logic seems backwards but it works  ¯\_(ツ)_/¯
    if Utils.process_running(process):
        return True
    else:
        return False
