import configparser
import subprocess
import time
import Event_checks

DEBUG = True
scoreReport = '/home/jdavis/Desktop/score.html'

class Pysel:

    def __init__(self, config_file):
        config_parser = configparser.ConfigParser()
        config_parser.read(config_file)
       
        self.events = {}
        self.currentScore = 0
        self.possibleScore = 0

        ## Parse the config
        for section in dict(config_parser._sections):
            self.events[section] = dict(config_parser._sections[section])
            if self.events[section]['enabled'] == 'yes':
                if int(self.events[section]['pointvalue']) > 0:
                    self.possibleScore += (int(self.events[section]['pointvalue']) * len(self.events[section]['parameters'].split()))
    
    def play_noise(self, file):
        pass
        #subprocess.call(["/usr/bin/aplay", file])

    def update_html(self):
        pass

    def send_notification(self):
        pass


    def start_engine(self):
        timeLeft = 180
        initialScore = 0
        while True:
            print('     +-------------------------------+')
            print('     |      PySEL Score Report:      |')
            print('     +-------------------------------+')
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
                            print('[X] ',event['pointvalue'], 'pts for',event['msg'], parameter )
                            self.currentScore += int(event['pointvalue'])
                        else:
                            if DEBUG == True and int(event['pointvalue']) > 0:
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
            print('You have', timeLeft, 'minutes remaining.\n\n')
            timeLeft -= 1
            time.sleep(5)
            
    
if __name__ == "__main__":
    Engine = Pysel("PySEL.conf")
    
    Engine.start_engine()