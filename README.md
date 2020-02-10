# PySEL - Python Scoring Engine: Linux

## Description
This is a rewrite of CSEL in Python. The engine was simplified from a GUI interface to a simple config file. PySEL was written in order to help cyberpatriot coaches and other teams create their own practice linux images. 

---
## Installation
1. Clone the repository
2. Change directory into repository
3. Edit the PySEL.conf file to score your flaws
4. Add execute permission on install script
5. Run the install script
   
```
git clone https://github.com/FWSquatch/pysel
chmod +x install.sh
./install.sh
```

---
## How to configure 
The PySEL.conf file only has a set amount of issues for ease of understanding we will reference issues as events. In order to score an event changed enabled to `yes`. Customize the category assigned to each flaw by changing the value of `tag`. If you want to change the point value of an event then change the `pointValue`. To deduct points make make the pointValue a negative value. Finally to customize the message on the score report change the value of `msg`. You may use the string `%PARAMETER%` to make pysel insert the parameter into your message.
  
An example event looks like: 
```
[01-GoodUsers:Required_Users]
enabled = yes
tag = User Management
pointValue = -10.0
parameters = user1 fred
description = Users that are required on the system
msg = Required user %PARAMETER% has been deleted!
```
### Breakdown
Each event will start with a title, the title consists of 2 parts: `[FlawID:Event]`  
The `FlawID` is a unique identifier for that instance of the flaw you are wanting to score. 
The `Event` correlates to a specific function that scores the event.  
The `parameters` of each event are passed to the function that gets called. If an event supports multiple parameters each parameters must be seperated by a space. Not all events supports multiple parameters. 

List of supported events:
- `Add_to_group`
- `Add_to_sudo.py`
- `Add_users.py`
- `Bad_file.py`
- `Check_forensics.py`
- `Check_password_policy`
- `Check_user_password`
- `Directory_no_longer_contains_string` 
- `Directory_now_contains_string`
- `File_no_longer_contains`
- `File_now_contains`
- `Firewall_enabled`
- `Firewall_rule_exists.py`
- `Kernel_harden`
- `Kernel_updated`
- `Not_owned_by_group`
- `Not_owned_by_user`
- `Owned_by_group`
- `Owned_by_user`
- `Package_updated_latest`
- `Package_updated_to_version`
- `Perm_no_longer_equal`
- `Perm_now_equal_to`
- `Prohibited_packages`
- `Prohibited_processes`
- `Prohibited_services`
- `Remove_from_group`
- `Remove_from_sudo`
- `Remove_users`
- `Required_packages`
- `Required_services`
- `Required_users`
- `Secure_lightdm`
- `Secure_login_defs`
- `Secure_ssh`
- `Update_settings`
Any of these events may be called more than once as long as you use unique FlawID's each time. For example, you may have two separate forensics events with unique messages:
```
[01-Forensics1:Check_forensics]
enabled = yes
tag  = Forensics
pointValue = 10
parameters = forensics1.txt:ssh 
description = Ex: forensic9.txt:green (Check forensic9.txt for ANSWER: green)
msg = Forensic question 1 correct
explanation = Here is an explanation for the flaw that will display if toggled on.

[02-Forensics2:Check_forensics]
enabled = yes
tag  = Forensics
pointValue = 10
parameters = forensics2.txt:oyeah
description = Ex: forensic9.txt:green (Check forensic9.txt for ANSWER: green)
msg = Forensic question 2 correct 
explanation = Here is an explanation for the flaw that will display if toggled on.
```

or you can put them into one FlawID that checks both:

```
[01-Forensics:Check_forensics]
enabled = yes
tag  = Forensics
pointValue = 10
parameters = forensics1.txt:example forensics2.txt:anotherone 
description = Ex: forensic9.txt:green (Check forensic9.txt for ANSWER: green)
msg = Forensic question %PARAMETER% is correct
explanation = Here is an explanation for the flaw that will display if toggled on.
```
---
## Development
If you are wanting to add a custom event you will need to follow some guidelines.  
- All event checks are stored in the `Event_checks` folder. 
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

After all of that is done you can add your custom event to the PySEL.conf file. 
```
[99-MyCustomFlaw:Check_hostname]
enabled = yes
tag = Custom Vulnerability
pointValue = 5
parameters = cyberpatriot
description = Make sure the hostname is set to "Cyberpatriot"
msg = Hostname has been changed to %PARAMETER%
explanation = The hostname of the system must be cyberpatriot according to the README file.
```
