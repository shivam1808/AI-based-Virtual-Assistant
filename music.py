import os 
import assistant_details as ad
import file_search


from pathlib import Path

my_file = Path("setup.py")
if my_file.is_file():
	import setup
	music_path = setup.music_path
else:
	music_path = 'E:\\Song'

songs = os.listdir(music_path)
		

def play_music():

	if ad.is_ubuntu():
		os.system("rhythmbox-client --play")
		return "Playing Music"

	else:		
		os.startfile(os.path.join(music_path, songs[0]))
		return "Playing Music"


def pause_music():
	
	if ad.is_ubuntu():
		os.system("rhythmbox-client --pause")
		return "Music Paused"

	else:
		return "For windows its not available"


def stop_music():
	
	if ad.is_ubuntu():
		os.system("rhythmbox-client --stop")
		return "Music Stoped"

	else:
		return "For windows its not available"

def next_song():
	
	if ad.is_ubuntu():
		os.system("rhythmbox-client --next")
		return "Playing Next Song"

	else:
		return "For windows its not available"

def previous_song():
	
	if ad.is_ubuntu():
		os.system("rhythmbox-client --previous")
		return "Playing Previous Song"

	else:
		return "For windows its not available"

def play_specific_song(song_name):
	song_name = song_name.replace('play ', '')
	if ad.is_ubuntu():
		file_search.set_root(music_path)
		songs = file_search.searchFile(song_name)
		try:
			song_uri = songs[0]
			command = 'rhythmbox-client --play-uri="' + song_uri + '"'
			os.system(command)
			return "Playing " + song_name
		except:
			return ("Song not found in your computer")

	else:
		file_search.set_root(music_path)
		songs = file_search.searchFile(song_name)
		try:
			os.startfile(os.path.join(music_path, songs[0]))
			return "Playing " + song_name
		except:
			return "Song not found in your computer"