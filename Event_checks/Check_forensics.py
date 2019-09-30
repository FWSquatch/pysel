from .Utils import Utils

def Check_forensics(file_answer):
    filename = file_answer.split(':')[0]
    answer = file_answer.split(':')[1]
    user = Utils.run_command("id -nu 1000").decode().rstrip()
    location = '/home/' + user + '/Desktop/' + filename 
    answer_string = 'ANSWER: ' + str(answer)
    if Utils.string_exists(location, answer_string):
        return True
    else:
        return False 