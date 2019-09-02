import re, subprocess, sys, os, time

class Event:
    def __init__(self, name, kw1, kw2, kw3, points, description, status):
        self.name = name
        self.kw1 = kw1
        self.kw2 = kw2
        self.kw3 = kw3
        self.points = points
        self.description = description
        self.status = status

def file_len(fname): # How many vulns are in the cfg file?
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

def read_config(configFile): # Read the cfg file into a list
    config = []
    f = open(configFile, "r")
    for line in f:        
        configLine = line.rstrip().split(',')
        config.append(configLine)
    return config

def string_exists(targetFile, searchString): # Search a targetFile for a searchString
    stringCount = 0
    try:
        f = open(targetFile,"r")
        for line in f:
            if re.search(searchString, line):
                stringCount += 1
        if stringCount > 0:
            return True
        else:
            return False
        f.close()
    except FileNotFoundError:
        return False

def check_firewall():
    proc = subprocess.Popen(['sudo', '/usr/sbin/ufw','status'], stdout=subprocess.PIPE)
    output = proc.stdout.read()
    if output == b'Status: active\n':
        return True
    else:
        return False

def draw_head(location):
    f = open(location,'w')
    f.write('<head><title>PySEL Score Report</title><meta http-equiv="refresh" content="40"></head><H2>Score Report</H2><br><table border="1"><tr><td>Pts</td><td>Event</td><td>Tag</td></tr>')
    f.close()

def draw_score(eventString): # Scoring Report Goodness.
    global debug
    global SCORE_REPORT_LOCATION
    f = open(SCORE_REPORT_LOCATION,'a')
    if eventString.status == "HIT":
        if int(eventString.points) < 0:
            fontcolor = '<tr><td><font color="red">'
        else:
            fontcolor = '<tr><td><font color="green">'
        scoreLine = fontcolor + str(int(eventString.points)) + "</td><td>" + eventString.description + "</font></td><td>" + eventString.kw3 + "</td></tr>"
        f.write(scoreLine)
    else:
        if debug == True:
            scoreLine = '<tr><td><font color="gray"> ' + str(int(eventString.points)) + "</td><td>" + eventString.description + "</font></td><td>" + eventString.kw3 + "</td></tr>"
            f.write(scoreLine)
    f.close()
    
def draw_tail(totalScore, possibleScore): # Draw the Score and Footer
    global SCORE_REPORT_LOCATION
    f = open(SCORE_REPORT_LOCATION,'a')
    totalLine = "</table><br><H3>Total Score: " + str(totalScore) + " out of " +str(possibleScore) + "<H3>"
    f.write(totalLine)

def check_event(eventString):
    addScore = 0
    if eventString.name == "baduser": # Score for removing bad users
        if bad_user(eventString.kw1):
            eventString.status = 'HIT'
            addScore = eventString.points
            print(eventString.points,eventString.description) # DEBUG
        else:
            eventString.status = 'MISS'    

    elif eventString.name == "gooduser": # Penalize for removing required users.
        if bad_user(eventString.kw1):# Same as baduser but with negative points.
            eventString.status = 'HIT'
            addScore = eventString.points
            print(eventString.points,eventString.description) # DEBUG
        else:
            eventString.status = 'MISS'

    elif eventString.name == "newuser": # Score for adding required users
        if new_user(eventString.kw1): 
            eventString.status = 'HIT'
            addScore = eventString.points
            print(eventString.points,eventString.description) # DEBUG
        else:
            eventString.status = 'MISS'

    elif eventString.name == "checkfirewall": # Is ufw firewall active?
        if check_firewall():
            eventString.status = 'HIT'
            addScore = eventString.points
            print(eventString.points,eventString.description) # DEBUG
        else:
            eventString.status = 'MISS'

    elif eventString.name == "addtofile":
        if string_exists(eventString.kw1, eventString.kw2):
            eventString.status = 'HIT'
            addScore = eventString.points
            print(eventString.points,eventString.description) # DEBUG
        else:
            eventString.status = 'MISS'

    elif eventString.name == "removefromfile":
        if string_exists(eventString.kw1, eventString.kw2):
            eventString.status = 'MISS'
        else:
            eventString.status = 'HIT'
            addScore = eventString.points
            print(eventString.points,eventString.description) # DEBUG

    elif eventString.name == "badprogram":
        if program_installed(eventString.kw1):
            eventString.status = 'MISS'
        else:
            eventString.status = 'HIT'
            addScore = eventString.points
            print(eventString.points,eventString.description) # DEBUG

    elif eventString.name == "goodprogram":
        if program_installed(eventString.kw1):
            eventString.status = 'HIT'
            addScore = eventString.points
            print(eventString.points,eventString.description) # DEBUG
        else:
            eventString.status = 'MISS'
    
    elif eventString.name == "groupadded":
        if string_exists('/etc/group', eventString.kw1):
            eventString.status = 'HIT'
            addScore = eventString.points
            print(eventString.points,eventString.description) # DEBUG
        else:
            eventString.status = 'MISS'
    
    elif eventString.name == "groupremoved":
        if string_exists('/etc/group', eventString.kw1):
            eventString.status = 'MISS'
        else:
            eventString.status = 'HIT'
            addScore = eventString.points
            print(eventString.points,eventString.description) # DEBUG
    
    elif eventString.name == "programversion":
        if check_program_version(eventString.kw1, eventString.kw2):
            eventString.status = 'HIT'
            addScore = eventString.points
            print(eventString.points,eventString.description) # DEBUG
        else:
            eventString.status = 'MISS'    
    
    elif eventString.name == "checkforensics":
        answer = 'ANSWER: ' + eventString.kw2
        if string_exists(eventString.kw1, answer):
            eventString.status = 'HIT'
            addScore = eventString.points
            print(eventString.points,eventString.description) # DEBUG
        else:
            eventString.status = 'MISS'
    
    elif eventString.name == "check4updates":
        updateInterval = 'APT::Periodic::Update-Package-Lists "' + str(eventString.kw1) + '";'
        if string_exists('/etc/apt/apt.conf.d/10periodic', updateInterval):
            eventString.status = 'HIT'
            addScore = eventString.points
            print(eventString.points,eventString.description) # DEBUG
        else:
            eventString.status = 'MISS'        

    elif eventString.name == "updateautoinstall":
        updateInterval = 'APT::Periodic::Unattended-Upgrade "' + str(eventString.kw1) + '";'
        if string_exists('/etc/apt/apt.conf.d/20auto-upgrades', updateInterval):
            eventString.status = 'HIT'
            addScore = eventString.points
            print(eventString.points,eventString.description) # DEBUG
        else:
            eventString.status = 'MISS'

    elif eventString.name == "useringroup":
        if user_in_group(eventString.kw1, eventString.kw2):
            eventString.status = 'HIT'
            addScore = eventString.points
            print(eventString.points,eventString.description) # DEBUG
        else:
            eventString.status = 'MISS'        
    
    elif eventString.name == "usernotingroup":
        if user_in_group(eventString.kw1, eventString.kw2):
            eventString.status = 'MISS'
        else:
            eventString.status = 'HIT'
            addScore = eventString.points
            print(eventString.points,eventString.description) # DEBUG
    elif eventString.name == "emptypassword":
        if empty_password(eventString.kw1):
            eventString.status = 'MISS'
        else:
            eventString.status = 'HIT'
            addScore = eventString.points
            print(eventString.points,eventString.description) # DEBUG            
    
    elif eventString.name == "badprocess":
        if service_running(eventString.kw1):
            eventString.status = 'MISS'
        else:
            eventString.status = 'HIT'
            addScore = eventString.points
            print(eventString.points,eventString.description) # DEBUG            

    elif eventString.name == "goodprocess":
        if service_running(eventString.kw1):
            eventString.status = 'HIT'
            addScore = eventString.points
            print(eventString.points,eventString.description) # DEBUG            
        else:
            eventString.status = 'MISS'

    elif eventString.name == "permequalto":
        if check_permissions(eventString.kw1) == eventString.kw2:
            eventString.status = 'HIT'
            addScore = eventString.points
            print(eventString.points,eventString.description) # DEBUG            
        else:
            eventString.status = 'MISS'

    elif eventString.name == "permnotequalto":
        if check_permissions(eventString.kw1) == eventString.kw2:
            eventString.status = 'MISS'            
        else:
            eventString.status = 'HIT'
            addScore = eventString.points
            print(eventString.points,eventString.description) # DEBUG

    elif eventString.name == "badfile":
        if os.path.exists(eventString.kw1):
            eventString.status = 'MISS'
        else:
            eventString.status = 'HIT'
            addScore = eventString.points
            print(eventString.points, eventString.description) # DEBUG

    else:
        print("unscoreable")
        draw_score(eventString)
    draw_score(eventString)
    return addScore
    
def bad_user(userName): # Check to see if baduser has been deleted
    if string_exists('/etc/passwd', userName):
        return False 
    else:
        return True

def new_user(userName): 
    if string_exists('/etc/passwd', userName):
        return True
    else:
        return False

def program_installed(program):
    proc = subprocess.Popen(['dpkg','--list'], stdout=subprocess.PIPE)
    output = proc.stdout.read().decode("utf-8")
    if program in output:
        return True
    else:
        return False

def check_program_version(programName, version):
    version = "Installed: " + version
    output = subprocess.check_output(["apt-cache", "policy", programName]).decode("utf-8")
    if version in output:
        return True
    else:
        return False

def user_in_group(userName, groupName):
    proc = subprocess.Popen(['grep', groupName, '/etc/group'], stdout=subprocess.PIPE)
    output = proc.stdout.read().decode("utf-8")
    if userName in output:
        return True
    else:
        return False

def empty_password(userName):
    blankPass = userName + "::"
    if string_exists('/etc/shadow',blankPass):
        return True
    else:
        return
        False

def service_running(serviceName):
    procFound = 0
    proc = subprocess.Popen(['ps','-ef'], stdout=subprocess.PIPE)
    output = proc.stdout.read().decode("utf-8")
    for line in output.split('\n'):
        if serviceName in line:
            procFound += 1
    if procFound > 0:
        return True
    else:
        return False

def check_permissions(fileName):
    proc = subprocess.Popen(['stat', '-c', '%A', fileName], stdout=subprocess.PIPE)
    output = proc.stdout.read().decode("utf-8")
    return(output.rstrip())

# Are we starting up in debug mode?
debug = False
if len(sys.argv) > 1:
    if sys.argv[1] == "--debug":
        debug = True   

# Instantiate objects
numEvents = len(master)
eventList = [Event('','','','',0,'','') for i in range(numEvents)]
for j in range(numEvents): 
    eventList[j].name = master[j][0]
    eventList[j].kw1 = master[j][1]
    eventList[j].kw2 = master[j][2]
    eventList[j].kw3 = master[j][3]
    eventList[j].points = master[j][4]
    eventList[j].description = master[j][5]
    eventList[j].status = master[j][6]

while True:
    possibleScore = 0
    totalScore = 0
    draw_head(SCORE_REPORT_LOCATION)
    for vulns in eventList:
        totalScore += int(check_event(vulns))
        if int(vulns.points) > 0:
            possibleScore += int(vulns.points)
    print(totalScore,"out of",possibleScore)
    draw_tail(totalScore, possibleScore)
    time.sleep(30)