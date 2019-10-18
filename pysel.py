import configparser
import subprocess
import time
import Event_checks
import hashlib
import requests

DEBUG = False
scoreReportLocation = ''

class Pysel:

    def __init__(self, config_file, team_conf):
        config_parser = configparser.ConfigParser()
        config_parser.read(config_file)
       
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
        print(self.general)
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

    def draw_html_head(self):
        f = open(self.general['General:Options']['scorereportlocation'], 'w')
        f.write('<!DOCTYPE html><html lang="en">\n<head><title>PySEL Score Report</title><meta http-equiv="refresh" content="40"></head>\n<body><table align="center"><tr><td><img src="/cyberpatriot/cplogo.png"></td><td><div align="center"><H1>PySEL</H1><H5>Python Scoring Engine: Linux</H5></div></td><td><img src="/cyberpatriot/eoclogo.png"</td></tr></table><br><hr><div align="center"><H2>Score Report</H2></div><br><table border="1"; align="center"><tr><td>Pts</td><td>Event</td><td>Tag</td></tr>\n')
        f.close()

    def update_html_body(self, score, event, parameter, tag):
        if score == 'MISS':
            payload = '<tr bgcolor="gray"><td>' + str(score) + '</td><td>' + str(event) + parameter + '</td><td>' + tag + '</td></tr>'
        else:
            if int(score) < 0:
                payload = '<tr bgcolor="red"><td>' + str(score) + '</td><td>' + str(event) + parameter + '</td><td>' + tag + '</td></tr>'
            else:
                payload = '<tr bgcolor="green"><td>' + str(score) + '</td><td>' + str(event) + parameter + '</td><td>' + tag + '</td></tr>'
            
        f = open(self.general['General:Options']['scorereportlocation'], 'a')
        f.write(payload)
        f.write('\n')
        f.close()
        pass

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
            self.draw_html_head()
            print('     +------------------------------+')
            print('     |      PySEL Score Report      |')
            print('     |       ' + self.general['General:Options']['remotereportinground'] + "        |")
            print('     +------------------------------+')

            self.currentScore = 0
            for name, event in self.events.items():
            
            ## parse the parameters list
                if event['enabled'] != "yes":
                    continue
                else:
                    params = event['parameters'].split(' ')
                    for parameter in params:
                        ## Eval the event to call the correct Event_checks function
                        if eval("Event_checks."+name.split(":")[1]+"(parameter)"):
                            print('[X] ',event['pointvalue'], 'pts for',event['msg'], parameter)
                            self.currentScore += int(event['pointvalue'])
                            self.update_html_body(event['pointvalue'], event['msg'], parameter, name.split(':')[0])
                        else:
                            if DEBUG == True and int(event['pointvalue']) > 0:
                                    self.update_html_body('MISS', event['msg'], parameter, name.split(':')[0])
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
            time.sleep(5)
            
    
if __name__ == "__main__":
    Engine = Pysel("PySEL.conf", "team.conf")
    
    Engine.start_engine()
