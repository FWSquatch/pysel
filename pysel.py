import configparser
import subprocess
import time
import Event_checks

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
            if int(self.events[section]['pointvalue']) > 0.0:
                self.possibleScore += int(self.events[section]['pointvalue']) 
     
    
    def play_noise(self, file):
        pass
        #subprocess.call(["/usr/bin/aplay", file])

    def update_html(self):
        pass

    def send_notification(self):
        pass


    def start_engine(self):
        events_scored = []
        while True:
            print("[*]Score Loop:\n [*]Current score: {} out of {}".format(self.currentScore, self.possibleScore))
            for name, event in self.events.items():
                ## Eval the event to call the correct Event_checks function
                ## parse the parameters list
                if event['enabled'] != "yes":
                    continue

                params = event['parameters'].split(' ')
                
                ## Events that reward points
                if int(event['pointvalue']) > 0:
                    if eval("Event_checks."+name.split(":")[1]+"(params)"):
                        if event in events_scored:
                            print("[*]Event already scored")
                        else:
                            events_scored.append(event)
                            print("[+]Point Scored:", name)
                            self.currentScore += int(event['pointvalue'])

                    ## If the event was previously scored and it is is no longer working
                    elif not eval("Event_checks."+name.split(":")[1]+"(params)") and event in events_scored:
                        print("[!]Previous gained score lost:", name)
                        self.currentScore -= int(event['pointvalue'])
                        for i,prev_event in enumerate(events_scored):
                            if prev_event == event:
                                del events_scored[i]

                ## Events that deduct points 
                elif int(event['pointvalue']) < 0:
                    if not eval("Event_checks."+name.split(":")[1]+"(params)"):
                        if event in events_scored:
                            print('[*]Event already scored')
                        else:
                            print("[!]Points lost:", name)
                            self.currentScore += int(event['pointvalue'])
                            events_scored.append(event)

                    elif eval("Event_checks."+name.split(":")[1]+"(params)") and event in events_scored:
                        print("[+]Previous lost score gained:", name) 
                        self.currentScore -= int(event['pointvalue'])
                        for i,prev_event in enumerate(events_scored):
                            if prev_event == event:
                                del events_scored[i]
            time.sleep(5)
    
if __name__ == "__main__":
    Engine = Pysel("Pysel.conf")
    
    Engine.start_engine()