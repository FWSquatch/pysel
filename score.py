s_config = """
[General:Options]
debug = yes
scoreReportLocation = /home/skills/Desktop/ScoreReport.html
remoteReportingenabled = no
remoteReportingServer = http://someserver.edu
remoteReportingRound = Some Competition
timeLimit = 150

[01-Forensics1:Owned_by_group]
enabled = yes
tag  = Forensics
pointValue = 10
parameters = /etc/passwd:root 
description = Ex: forensic9.txt:green (Check forensic9.txt for ANSWER: green)
msg = File owned by root

[02-Forensics2:Check_forensics]
enabled = no
tag  = Forensics
pointValue = 10
parameters = forensics2.txt:oyeah
description = Ex: forensic9.txt:green (Check forensic9.txt for ANSWER: green)
msg = Forensic question 2 correct 

[03-BadUsers:Remove_users]
enabled = no
tag = User Management
pointValue = 5
parameters = plankton
description = Users that should be removed from the system 
msg = Unwanted user %PARAMETER% has been removed: 

[04-NewUsers:Add_users]
enabled = no
tag = User Management
pointValue = 5
parameters = sandy
description = Users that need to be added to the system
msg = New user %PARAMETER% added to system 

[05-GoodUsers:Required_users]
enabled = no
tag = User Management
pointValue = -10
parameters = root cyber squidward
description = Users that are required on the system
msg = Essential user %PARAMETER% has been removed!

[06-RequiredSudo:Add_to_sudo]
enabled = no
tag = User Management
pointValue = 6
parameters = eugene
description = Users that are required to be Administrators
msg = User %PARAMETER% is now an administrator

[07-UnauthorizedSudo:Remove_from_sudo]
enabled = no
tag = User Management
pointValue = 6
parameters = spongebob
description = Users that are prohibited from being Administrators
msg = User %PARAMETER% is no longer an administrator

[08-RequiredInGroup:Add_to_group]
enabled = no
tag = User Management
pointValue = 6
parameters = spongebob:krustyk squidward:krustyk sandy:krustyk
description = Users that are required to be in a group
msg = User %PARAMETER% is now in group

[09-UnauthorizedInGroup:Remove_from_group]
enabled = no
tag = User Management
pointValue = 6
parameters = plankton:krustyk spongebob:krustyk
description = Users that are prohibited from being in a group
msg = User %PARAMETER% is no longer in group

[10-DisableGuestEtc:Secure_lightdm]
enabled = yes
tag = User Management
pointValue = 5
parameters = allow-guest greeter-hide-users greeter-show-manual-login
description = 
msg = Guest account has been disabled

[11-CheckUserPassword: Check_user_password]
enabled = no
tag = User Management
pointValue = 5
parameters = sandy:MinDays spongebob:MaxDays squidward:NoPassword
description = Ex: username:check. Possible parameters MinDays, MaxDays, NoPassword
msg = Password issue has been fixed: %PARAMETER%

[12-PasswordPolicy:Check_password_policy]
enabled = no
tag = Account Policy
pointValue = 5
parameters = RejectUsername EnforceForRoot LockoutTally MinLen:6 Retry:5 MaxRepeat:3 Remember:12 UCredit:1 LCredit:1 DCredit:1 DifOk:3 GecosCheck:1
description = Possible parameters RejectUsername, EnforceForRoot, LockoutTally, MinLen:#, Retry:#, MaxRepeat:#, Remember:#, UCredit:#, LCredit:#, DCredit:#, DifOk:#, GecosCheck:1
msg = Password policy %PARAMETER% secured

[####13-LockoutPolicy:Check_account_lockout]
enabled = no
tag = Account Policy
pointValue = 5
parameters = OnErrorFail Audit EvenDenyRoot Deny:5 UnlockTime:1200 RootUnlockTime:1200
description = Possible parameters 
msg = Account lockout policy secured by %PARAMETER%

[14-LoginDefs:Secure_login_defs]
enabled = no
tag = Account Policy
pointValue = 5
parameters = PasswordMaxDays PasswordMinDays PasswordWarnAge LogUnknownFail LogOkLogins SuLogFile
description = Possible parameters: PasswordMaxDays, PasswordMinDays, PasswordWarnAge, LogUnknownFail, LogOkLogins, SuLogFile
msg = Account policy has been made more secure by %PARAMETER%

[15-CowsayInstalled:Required_packages]
enabled = no
tag = Application Update
pointValue = 7
parameters = cowsay
description = Packages that must be present on the system
msg = Required package %PARAMETER% has been installed

[16-GitUpdate:Package_updated_latest]
enabled = no
tag = Application Update
pointValue = 5
parameters = git
description = Package that has been updated to the latest version
msg = Package %PARAMETER% has been updated

[16-SpecialFirefox:Package_updated_to_version]
enabled = no
tag = Application Update
pointValue = 5
parameters = firefox:54.0+build3-0ubuntu0.16.04.1 nano:2.5.3-2
description = Package that has been updated to THIS SPECIFIC VERSION
msg = Package has updated: %PARAMETER%

[17-RemoveHydraJohn:Prohibited_packages]
enabled = no
tag = Unwanted Software
pointValue = 7
parameters = cowsay
description = Packages that are not allowed on the system
msg = Unwanted software %PARAMETER% removed

[18-ShieldsUP:Firewall_enabled]
enabled = no
tag = Defensive Countermeasures
pointValue = 4
parameters = None
description = Make sure the firewall is enabled
msg = Firewall protection has been enabled

[19-SecureSSH:Secure_ssh]
enabled = no
tag = Application Security
pointValue = 4
parameters = defaultPortChange PermitRootLoginNo Protocol2Only UsePAMyes PermitUserEnvironmentNo PermitEmptyPasswordsNo
description = Possible parameters: defaultPortChange, PermitRootLoginNo, Protocol2Only, UsePAMyes, PermitUserEnvironmentNo PermitEmptyPasswordsNo
msg = SSH made more secure by %PARAMETER%

[20-SshRequiredService:Required_services]
enabled = no
tag = Service Auditing
pointValue = 7
parameters = ssh
description = Services that must be running
msg = Required service %PARAMETER% is running

[21-BadServiceApache2:Prohibited_services]
enabled = no
tag = Service Auditing
pointValue = 7
parameters = apache2 nc
description = Services that you want stopped
msg = Service %PARAMETER% has been disabled

[21A-Netcat:Prohibited_processes]
enabled = no
tag = Malware
pointValue = 7
parameters = nc
description = Processes that you want stopped
msg = Service %PARAMETER% has been stopped

[22-KernelNoLonger4.12:Kernel_updated]
enabled = no
tag = OS Updates
pointValue = 5
parameters = 4.10.0-28-generic
description = Check to see if the kernel has been updated
msg = Linux kernel has been updated

[23-TurnOnUpdates:Update_settings]
enabled = no
tag = OS Update
pointValue = 4
parameters = installSecUpdates checkDaily downloadSecUpdates notifyForLTS mainRepoEnabled
description = Possible parameters: installSecUpdates checkDaily, downloadSecUpdates, notifyForLTS, mainRepoEnabled
msg = Update settings have been configured: 

[####24-SysCtrlGoodness:Kernel_harden]
enabled = no
tag = Local Policy
pointValue = 5
parameters = BlockModLoading DmesgRestrict KexecLoadDisabled UnprivBpfDisabled CoreUsesPid CtrlAltDel SysRq AllRejectAcceptRedirects DefRejectAcceptRedirects AllDisableAcceptSourceRoute DefDisableAcceptSourceRoute BootPReplay Ipv4Forwarding AllLogMartians DefLogMartians McForwarding ProxyArp RpFilter DisableSendRedirects IgnoreIcmpBroadcast IgnoreIcmpBogusError TcpSynCookies TcpTimestamps DisableUnprivUserNameSpace
description = Possible Parameters: BlockModLoading, DmesgRestrict, KexecLoadDisabled, UnprivBpfDisabled, CoreUsesPid, CtrlAltDel, SysRq, AllRejectAcceptRedirects, DefRejectAcceptRedirects, AllDisableAcceptSourceRoute, DefDisableAcceptSourceRoute, BootPReplay, Ipv4Forwarding, AllLogMartians, DefLogMartians, McForwarding, ProxyArp, RpFilter, DisableSendRedirects, IgnoreIcmpBroadcast, IgnoreIcmpBogusError, TcpSynCookies, TcpTimestamps, DisableUnprivUserNameSpace
msg = Kernel hardened via %PARAMETER%

[25-ChangePermShadow:Perm_no_longer_equal]
enabled = no
tag = Uncategorized OS Setting
pointValue = 8
parameters = /etc/shadow:777
description = Ex: /etc/shadow:777 (Change permissions of /etc/shadow away from 777
msg = File permissions on /etc/shadow have been secured

[26-ChangePermSshConfig:Perm_now_equal_to]
enabled = no
tag = Uncategorized OS Setting
pointValue = 8
parameters = /etc/ssh/sshd_config:600
description = Ex: /etc
msg = File permissions on /etc/sshd_config have been secured

[27-RemoveDummyMp3Prohibited Files:Bad_file]
enabled = no
tag = Prohibited File
pointValue = 5
parameters = /opt/dummy.mp3
description = Files you want removed from the system
msg = Prohibited file %PARAMETER% removed

[28-SomeMiscThing:File_no_longer_contains]
enabled = no
tag = Local Policy
pointValue = 5
parameters = /opt/file1:^Hello
description = Text you would like removed from file (Regex is allowed)
msg = File /etc/example has changed in some way. (text removed)

[29-SomeMiscThing:File_now_contains]
enabled = no
tag = Local Policy
pointValue = 5
parameters = /opt/file2:Hello
description = Text you would like added to file
msg = File /etc/example2 has changed in some way (text added)

[07-SwansonNoPasswdLogin:File_no_longer_contains]
enabled = no
tag = Local Policy
pointValue = 5
parameters = /home/cyber/Desktop/group:^nopasswdlogin.*rswanson.*
description = Text you would like removed from file
msg = File /etc/example has changed in some way. (text removed)

[08-SwansonNoPasswdLogin:File_no_longer_contains]
enabled = no
tag = Local Policy
pointValue = 5
parameters = /home/cyber/Desktop/group:(?:libpam-cracklib|libpam-pwquality)
description = Text you would like removed from file
msg = File /etc/example has changed in some way. (text removed)

"""
import configparser
import subprocess
import time
import Event_checks
import hashlib
import requests
from collections import OrderedDict
import os
import io

DEBUG = False
scoreReportLocation = ''
teamIdLocation = '/usr/local/bin/pysel/TEAM'

## Dump your config here in order to test without installing
"""
s_config = 
[General:Options]
debug = yes
scoreReportLocation = /home/jdavis/Desktop/ScoreReport.html
remoteReportingenabled = no
remoteReportingServer = http://moodle.centraltech.edu
remoteReportingRound = OK-Cup-StateRd-Ub16
timeLimit = 150

[10-DisableGuestEtc:Secure_lightdm]
enabled = yes
tag = User Management
pointValue = 5
parameters = allow-guest greeter-hide-users greeter-show-manual-login
description = 
msg = Guest account has been disabled
"""

class Pysel:

    def __init__(self, s_file, team_conf):
        buf = io.StringIO(s_file)
        config_parser = configparser.ConfigParser()
        config_parser.read_file(buf)
#        config_parser = configparser.ConfigParser()
#        config_parser.read(buf)
       
        team_config = configparser.ConfigParser()
        team_config.read(team_conf)

        self.events = {}
        self.general = {}
        self.team_config = {}
        self.currentScore = 0
        self.possibleScore = 0

        ## Parse team config
        for section in dict(team_config._sections):
            if section == "Team":
                self.team_config[section] = dict(team_config._sections[section])
        ## Parse the config
        for section in dict(config_parser._sections):
            if section == 'General:Options':  ## Look at the general options
                self.general[section] = dict(config_parser._sections['General:Options'])
            else:
                self.events[section] = dict(config_parser._sections[section])
                if self.events[section]['enabled'] == 'yes':
                    if int(self.events[section]['pointvalue']) > 0:
                        self.possibleScore += (int(self.events[section]['pointvalue']) * len(self.events[section]['parameters'].split()))
        self.sortedEvents = OrderedDict(sorted(self.events.items()))
        
        if self.general['General:Options']['debug'] == 'yes':
            global DEBUG
            DEBUG = True
        
    
    def __hash_score__(self, score):
        hashstring = str(score) + 'qwerty'
        hashedval = hashlib.md5(hashstring.encode('utf-8').rstrip())

        return hashedval

    def play_noise(self, file):
        pass
        #subprocess.call(["/usr/bin/aplay", file])

    def draw_html_head(self, team, round):
        f = open(self.general['General:Options']['scorereportlocation'], 'w')
        f.write('<!DOCTYPE html><html lang="en">\n<head><title>PySEL Score Report</title><meta http-equiv="refresh" content="40"></head>\n<body><table align="center"><tr><td><img src="/cyberpatriot/cplogo.png"></td><td><div align="center"><H1>Oklahoma</H1><H5>Cybersecurity Competition</H5></div></td><td><img src="/cyberpatriot/eoclogo.png"</td></tr></table><br><hr><br><table border="1"; align="center"><tr><td colspan=3><div align="center"><b>Team: ' + team + '&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Round: ' + round + '</b></div></td></tr><tr><td>Pts</td><td>Event</td><td>Tag</td></tr>\n')
        f.close()

    def update_html_body(self, score, event, parameter, tag):
        if '%PARAMETER%' not in event:
          reportedEvent = event
        else:
          reportedEvent = str(event).replace('%PARAMETER%', parameter)
        if score == 'MISS':
             payload = '<tr bgcolor="lightgray"><td>' + str(score) + '</td><td>' + reportedEvent + '</td><td>' + tag + '</td></tr>'

        else:
            if int(score) < 0:
                payload = '<tr bgcolor="crimson"><td>' + str(score) + '</td><td>' + reportedEvent + '</td><td>' + tag + '</td></tr>'
            else:
                payload = '<tr bgcolor="lightgreen"><td>' + str(score) + '</td><td>' + reportedEvent + '</td><td>' + tag + '</td></tr>'
            
        f = open(self.general['General:Options']['scorereportlocation'], 'a')
        f.write(payload)
        f.write('\n')
        f.close()

    def get_team_id(self, teamIdLocation):
        if os.path.exists(teamIdLocation):
            f = open(teamIdLocation, 'r')
            team = f.readline()
        else:
            team = '<font color="red">NO TEAM!</font>'
        return (team)

    def draw_html_tail(self, currentScore, totalScore):
        f = open(self.general['General:Options']['scorereportlocation'], 'a')
        payload = '</table><div align="center"><br><H3>Total Score: ' + currentScore + ' out of ' + totalScore + '</H3></div><hr><br>\n<div align="center">Last updated: ' + str(time.ctime()) + '</div></body></html>'
        f.write(payload)
        f.close()


    def send_notification(self):
        pass


    def start_engine(self):
        timeLeft = int(self.general['General:Options']['timelimit'])
    
        initialScore = 0
        while True:
            self.draw_html_head(self.get_team_id(teamIdLocation), self.general['General:Options']['remotereportinground'])
            # print('     +------------------------------+')
            # print('     |      PySEL Score Report      |')
            # print('     |       ' + self.general['General:Options']['remotereportinground'] + "        |")
            # print('     +------------------------------+')

            self.currentScore = 0
            for name, event in self.sortedEvents.items():
            
            ## parse the parameters list
                if event['enabled'] != "yes":
                    continue
                else:
                    params = event['parameters'].split(' ')
                    for parameter in params:
                        ## Eval the event to call the correct Event_checks function
                        if eval("Event_checks."+name.split(":")[1]+"(parameter)"):
                            print('[X] ',event['pointvalue'], 'pts for',event['tag'], parameter)
                            self.currentScore += int(event['pointvalue'])
                            self.update_html_body(event['pointvalue'], event['msg'], parameter, event['tag'])
                        else:
                            if DEBUG == True and int(event['pointvalue']) > 0:
                                    self.update_html_body('MISS', event['msg'], parameter, event['tag'])
                                    print("[ ]  0 pts for",event['msg'], parameter)
            
            ## Did we gain or lose points?
            if initialScore < self.currentScore:
                print("_____I LIKE YOUR STYLE!____")
                self.play_noise('/cyberpatriot/gain.wav')
            elif initialScore > self.currentScore:
                print("_____YOU DISGUST ME!____")
                self.play_noise('/cyberpatriot/lose.wav')

            initialScore = self.currentScore
            print('Current score: {} out of {}'.format(self.currentScore, self.possibleScore))
            self.draw_html_tail(str(self.currentScore), str(self.possibleScore))

            if self.general['General:Options']['remotereportingenabled'] == "yes":
                url = self.general['General:Options']['remotereportingserver']
                url += "/ss/ss.php?mode=send&game=okcyberrun_r1&team={self.team['team_id']}&player={self.general['General:Options']['remotereportinground']}&score={str(self.currentScore)}&md5={str(self.__hash_score__(self.currentScore))}"
                print('sending', url)
                r = requests.get(url) 
                print(r.status_code, r.text) 

            print('You have', timeLeft, 'minutes remaining.\n\n')
            timeLeft -= 1
            time.sleep(60)
            
 
if __name__ == "__main__":
    Engine = Pysel(s_config, "team.conf")
    
    Engine.start_engine()
