# PySEL - Python Scoring Engine: Linux

## Description
This is a rewrite of CSEL in Python. The engine was simplified from a GUI interface to a simple config file. PySEL was written in order to help cyberpatriot coaches and other teams create their own practice linux images. 

---
## Installation
1. Clone the repository
2. Change directory into repository
3. Add execute permission on install script
4. Run the install script
   
```
git clone https://github.com/FWSquatch/pysel
chmod +x install.sh
./install.sh
```

---
## How to configure 
The PySEL.conf file only has a set amount of issues for ease of understanding we will reference issues as events. In order to score an event changed enabled to `yes`. If you want to change the point value of an event then change the `pointValue`. To deduct points make make the pointValue a negative value. Finally to customize the message on the score report change the value of `msg`.
  
An example event looks like: 
```
[User Management:Required_Users]
enabled = yes
pointValue = -10.0
parameters = user1 user2
description = Users that are required on the system
msg = 
```
### Breakdown
Each event will start with a title, the title consists of 2 parts: `[Category:Event]`  
The `Event` correlates to a specific function that scores the event.  
The `parameters` of each event are passed to the function that gets called. If an event supports mulple parameters each parameters must be seperated by a space. Not all events supports multiple parameters. 

List of events that support multiple parameters:
- `[Forensics:Check_forensics]`
- `[User Auditing:Remove_users]`
- `[User Auditing:Add_users]`
- `[User Auditing:Required_users]`
- `[Account Policy:Secure_login_defs]`
- `[Application Upate:Required_packages]`
- `[Unwanted Software:Prohibited_packages]`
- `[Application Security:Secure_ssh]`
- `[Service Auditing:Required_services]`
- `[Service Auditing:Prohibited_services]`
- `[User Auditing:Remove_from_group]`
- `[User Auditing:Add_to_group]`
- `[Uncatagorized OS Setting:Perm_no_longer_equal]`
- `[Uncatagorized OS Setting:Perm_now equal_to]`


---
## Development
If you are wanting to add a custom event you will need to follow some guidelines.  
All event checks are stored in the Event_checks folder. 
- In order to score points the event should return `True`
- The event must only return `True` or `False`.  
- By default the return value should be `False`. 
- Functions in `Utils.py` are avilable and can be imported by adding `from .Utils import Utils`
  
An example custom event should look similar to this:
  
Filename: `Check_hostname.py`
```
from .Utils import Utils
## The hostname is passed from the parameters
def Check_hostname(hostname):
    if Utils.run_command('cat /etc/hostname') == hostname:
        return True
    else:
        return False
```

- Once you have the function written add `from .Check_hostname import Check_hostname` to the bottom of `__init__.py`


After all of that is done you can add your custom event to the PySEL.conf file. 
```
[Custom Events: Check_hostname]
enabled = yes
pointValue = 5
parameters = Cyberpatriot
description = Make sure the hostname is set to "Cyberpatriot"
```