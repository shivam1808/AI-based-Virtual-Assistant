import os.path, time
import os
from database import get_last_modify, update_last_modify

files = "input\\intents.json"
last_modify =  time.ctime(os.path.getmtime(files))

def check_last_modify():
    memory_last_modify = get_last_modify()
    if last_modify == memory_last_modify:
        print("Model is updated.")
    
    else:
        print("Wait for few seconds while I update the model")
        cmd = 'pythonw Model_train.py'
        os.system(cmd)
        update_last_modify(last_modify)
        print("Model Updated. Thank you!!!")