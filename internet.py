import urllib.request
import wikipedia 

def check_internet_connection():

    try:
        urllib.request.urlopen('http://google.com') #Python 3.x
        return True
    except:
        return False


def check_on_wikipedia(query):
	query = query.lower()

	query = query.replace("who is", "")
	query = query.replace("what is", "")
	query = query.replace("do u know who is", "")
	query = query.replace("tell me about", "")

	query = query.strip()

	try:
		data = wikipedia.summary(query, sentences=2)
		data = "According to wikipedia "+data
		return data
	except Exception as e:
		return ""
