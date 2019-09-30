from .Utils import Utils

def Update_settings(setting):
    if setting  == 'installSecUpdates':
        if Utils.string_exists('/etc/apt/sources.list', '^deb.*security.*'):
            return True
        else:
            return False        
    elif setting == 'checkDaily':
        if Utils.string_exists('/etc/apt/apt.conf.d/10periodic', 'APT::Periodic::Update-Package-Lists "1";'):
            return True
        else:
            return False
    elif setting == 'downloadSecUpdates':
        if Utils.string_exists('/etc/apt/apt.conf.d/10periodic', 'APT::Periodic::Download-Upgradeable-Packages "1";'):
            return True
        else:
            return False
    elif setting == 'notifyForLTS':
        if Utils.string_exists('/etc/update-manager/release-upgrades', 'Prompt=lts'):
            return True
        else:
            return False        
    elif setting == 'mainRepoEnabled':
        if Utils.string_exists('/etc/apt/sources.list', '^deb.*main$'):
            return True
        else:
            return False        
