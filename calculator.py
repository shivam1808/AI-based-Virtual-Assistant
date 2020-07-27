import wolframalpha

app_id = "6VUT62-AEXY978HH5" 
client = wolframalpha.Client(app_id) 

def calculator(inp):
    indx = inp.lower().split().index('calculate') 
    query = inp.split()[indx + 1:] 
    res = client.query(' '.join(query)) 
    answer = next(res.results).text 
    return ("The answer is " + answer) 