from .Utils import Utils

def Prohibited_services(service):
    if Utils.service_running(service):
        return False
    else:
        return True
