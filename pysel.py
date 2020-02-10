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
EXPLAIN = False
scoreReportLocation = ''
teamIdLocation = '/usr/local/bin/pysel/TEAM'

## Dump your config here in order to test without installing
# s_config = """ """

class Pysel:

    def __init__(self, s_file, team_conf):
        buf = io.StringIO(s_file)
        config_parser = configparser.ConfigParser()
        config_parser.read_file(buf)
       
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
        if self.general['General:Options']['explanations'] == 'yes':
            global EXPLAIN
            EXPLAIN = True
        
    
    def __hash_score__(self, score):
        hashstring = str(score) + 'qwerty'
        hashedval = hashlib.md5(hashstring.encode('utf-8').rstrip())

        return hashedval

    def play_noise(self, file):
        pass
        #subprocess.call(["/usr/bin/aplay", file])

    def draw_html_head(self, team, round):
        f = open(self.general['General:Options']['scorereportlocation'], 'w')
        f.write('<!DOCTYPE html><html lang="en">\n<head><title>PySEL Score Report</title><meta http-equiv="refresh" content="40"></head>\n<body><table width="600"; align="center";><tr><td><img src="/pysel-static/cplogo.png"></td><td><div align="center"><H1>Oklahoma</H1><H5>Cybersecurity Competition</H5></div></td><td><img src="/pysel-static/eoclogo.png"</td></tr></table><br><hr><br><table border="1"; align="center"; width="900"><tr><td colspan=3><div align="center"><b>Team: ' + team + '&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Round: ' + round + '</b></div></td></tr><tr><td>Pts</td><td>Event</td><td>Tag</td></tr>\n')

        f.close()

    def update_html_body(self, score, event, parameter, tag, explanation):
        if '%PARAMETER%' not in event:
          reportedEvent = event
        else:
          reportedEvent = str(event).replace('%PARAMETER%', parameter)
        if score == 'MISS':
             payload = '<tr bgcolor="lightgray"><td>' + str(score) + '</td><td>' + reportedEvent + '</td><td>' + tag + '</td></tr>'
             if EXPLAIN == True:
                 payload += '<tr bgcolor="lightgray"><td colspan="3">' + explanation + '</td></tr>'

        else:
            if int(score) < 0:
                payload = '<tr bgcolor="crimson"><td>' + str(score) + '</td><td>' + reportedEvent + '</td><td>' + tag + '</td></tr>'
            else:
                payload = '<tr bgcolor="lightgreen"><td>' + str(score) + '</td><td>' + reportedEvent + '</td><td>' + tag + '</td></tr>'
                if EXPLAIN == True:
                    payload += '<tr bgcolor="lightgreen"><td colspan="3">' + explanation + '</td></tr>'
            
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
                            self.update_html_body(event['pointvalue'], event['msg'], parameter, event['tag'], event['explanation'])
                        else:
                            if DEBUG == True and int(event['pointvalue']) > 0:
                                    self.update_html_body('MISS', event['msg'], parameter, event['tag'], event['explanation'])
                                    print("[ ]  0 pts for",event['msg'], parameter)
            
            ## Did we gain or lose points?
            if initialScore < self.currentScore:
                print("_____I LIKE YOUR STYLE!____")
                self.play_noise('/pysel-static/gain.wav')
            elif initialScore > self.currentScore:
                print("_____YOU DISGUST ME!____")
                self.play_noise('/pysel-static/lose.wav')

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
