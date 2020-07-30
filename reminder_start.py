import  os 

def remind(s):
    cmd = 'pythonw reminder.py "' + s + '"'
    os.system(cmd)
    return "Reminder Set"