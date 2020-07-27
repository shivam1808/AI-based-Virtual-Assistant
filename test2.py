import re
import wikipedia

command = "tell me about modi"
reg_ex = re.search('tell me about (.*)', command)
try:
    if reg_ex:
        topic = reg_ex.group(1)
        ny = wikipedia.page(topic)
        print(ny.content[:500].encode('utf-8'))
except Exception as e:
        print(e)