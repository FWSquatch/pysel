from .Utils import Utils

def Required_services(service):
    if Utils.service_running(service):
        return True
    else:
        return False