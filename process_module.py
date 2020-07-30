from time_details import get_time, get_date
from database import *
from input_module import take_input
from output_module import output
from internet import check_internet_connection, check_on_wikipedia
import assistant_details
from music import *
import os
import random

from web import open_facebook, open_google, close_browser, open_youtube_song, search_google, search_youtube
from display import change_wallpaper
from news import get_news
from weather import check_weather
from calculator import calculator
from send_text import sending_text
from games import play_game
from location import get_location
from nearby import search_near
from direction import directions

from send_email import sending_mail
from reminder_start import remind

from AIBot import response
from help_task import help
from umbrella_need import umbrella

def  process(query):

	query = query.lower()
	name = assistant_details.name
	query = query.replace(name, "")

	noAnswer = ["Sorry, can't understand you", "Please give me more info", "Not sure I understand"]

	if len(query)<=1:
		return random.choice(noAnswer)

	if "quit" in query:
		umbrella()
		output("Thank You!!! See You Soon")
		exit()
	
	if query == "--help" or query == "--h":
		help(query)
		return "What can I do for you?"

	if "game" in query:
		answer = get_answer_from_memory("play game")

	elif 'play' in query and 'music' not in query and 'songs' not in query:
		answer = get_answer_from_memory("play")

	elif 'weather' in query:
		answer = get_answer_from_memory("weather")

	elif 'location' in query:
		answer = get_answer_from_memory("location")

	elif 'search' in query:
		answer = get_answer_from_memory("search")

	elif 'send mail' in query or 'send email' in query:
		answer = get_answer_from_memory("send email")

	elif 'calculate' in query:
		answer = get_answer_from_memory("calculate")

	elif 'map' in query:
		answer = get_answer_from_memory("google map")

	elif 'remind me' == query.lower() or 'alarm' in query.lower():
		if 'remind me' == query.lower():
			output("Enter msg to remind")
			msg = take_input()
			output("Enter time(like 11:15)")
			time = take_input()
			output("Enter date(like 21 july)")
			date = take_input()
			res = 'remind me to ' + msg + 'at ' + time + 'on ' + date
			
			return remind(res)

		else:
			msg = "Alarm"
			output("Enter time(like 11:15)")
			time = take_input()
			output("Enter date(like 21 july)")
			date = take_input()
			res = 'remind me to ' + msg + 'at ' + time + 'on ' + date
			remind(res)
			return "Alarm Set"
	elif 'remind me' in query.lower():
		answer = get_answer_from_memory("remind me")
	else:
		answer = get_answer_from_memory(query)

	# print("answer - ", answer)

	# Check query

	if answer == "get time details":
		return ('Time is '+ get_time())

	elif answer == "change name":
		output("Okay! what do u want to call me")
		temp = take_input()
		if temp == assistant_details.name:
			return "Can't change. I think you are happy with my old name"
		else:
			update_name(temp)
			assistant_details.name = temp
			return "Now you can call me " + temp

	elif answer == "tell date":
		return "Date is " + get_date()

	elif answer == "on speak":
		return turn_on_speech()

	elif answer == "off speak":
		return turn_off_speech()

	elif answer == "on listen":
		return turn_on_listen()

	elif answer == "off listen":
		return turn_off_listen()

	elif answer == "play game":
		return play_game()

	elif answer == "open facebook":
		open_facebook()
		return "opening facebook"

	elif answer == "open google":
		open_google()
		return "opening google"

	elif answer == "close browser":
		close_browser()
		return "closing browser"

	elif answer == "check internet connection":
		if check_internet_connection():
			return "Internet is Connected"
		else:
			return "Internet Not Connected"

	elif answer == "play music":
		return play_music()

	elif answer == "pause music":
		return pause_music()

	elif answer == "stop music":
		return stop_music()

	elif answer == "next song":
		return next_song()

	elif answer == "previous song":
		return previous_song()

	elif answer == "play":
		music = play_specific_song(query)
		if "not found" in music:
			output("Song not found, Should i search on youtube!")
			res = take_input()
			if "yes" in res.lower():
				open_youtube_song(query.replace('play ', ''))
				return ("Searching on YouTube")
			else:
				return ('Okay')
		else:
			return music
	
	elif answer == 'search':
		if 'youtube' in query:
			query = query.replace('search ','')
			query = query.replace(' on youtube', '')
			search_youtube(query)
			return "Searching youtube"
		else:
			query = query.replace('search ','')
			query = query.replace(' google', '')
			query = query.replace(' on google', '')
			search_google(query)
			return "Searching Google"

	elif answer == "change wallpaper":
		return change_wallpaper()

	elif answer == "get news":
		return get_news()

	elif answer == "weather":
		place = query.replace('weather', '')
		return check_weather(place)

	elif answer == "location":
		return get_location()

	elif answer == "nearby":
		query = query.replace('nearby ', '')
		return search_near(query)

	elif answer == 'calculate':
		return calculator(query)

	elif answer == "map":
		indx = query.lower().split().index('map')
		que = query.split()[indx + 1:]
		cmd =  'python map.py ' + ' '.join(que)
		os.system(cmd)
		return "Opening Google Map"

	
	elif answer == "direction":
		output("Start location (if current location leave blank)")
		start_place = take_input() 
		output("Destination")
		end_place = take_input()
		if start_place == None:
			return directions(end_place)
		else:
			return directions(end_place, start_place)

	elif answer == "mail":
		name = query.replace("send email to ", "")
		mail = get_emailId(name)
		if mail == '0':
			output("Email Id not found in database, please input mail id")
			mail = take_input()
			insert_emailId(name, mail)
			output("mail id inserted to database")

		output("Enter message to send to "+name)
		msg = take_input()

		return sending_mail(name, mail, msg)

	elif answer == "send msg":
		output("Enter Contact Number ")
		number = take_input()
		output("Enter message to send to " + number)
		msg = take_input()

		return sending_text(msg, number)

	elif answer == 'remind me':
		remind(query)
		return "Reminder Set"

	else:
		res = response(query)
		if res != '0':
			return res
		
		else:
			output("Dont know this one should i search on internet?")
			ans = take_input()
			if "yes" in ans:
				output("Searching Wikipedia...")
				answer = check_on_wikipedia(query)
				if answer != "":
					return answer
			else:

				output("Can you please tell me what it means?")
				ans = take_input()
				if "it means" in ans:
					ans = ans.replace("it means", "")
					ans = ans.strip()

					value = get_answer_from_memory(ans)

					if value == "":
						return "Can't help with this one"

					else:
						insert_question_and_answer(query, value)
						return "Thanks, I will remember it for the next time"

				else:
					return "Can't help with this one"

			return "Nothing"