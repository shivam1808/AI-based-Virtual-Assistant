import webbrowser
import os
from youtube_search import YoutubeSearch

def open_facebook():
	webbrowser.open("https://facebook.com")

def open_google():
	webbrowser.open("https://google.com")

def open_youtube_song(song_name):
    results = YoutubeSearch(song_name, max_results=1).to_dict()
    url = "https://www.youtube.com/" + results[0]['url_suffix']
    webbrowser.open(url)
    

def search_youtube(search):
    query = '+'.join(search.split())
    url = "https://www.youtube.com/results?search_query=" + query
    webbrowser.open(url)


def search_google(search):
    query = '+'.join(search.split())
    url = "https://www.google.com/search?q=" + query
    webbrowser.open(url)

def close_browser():
	os.system('pkill chrome')
