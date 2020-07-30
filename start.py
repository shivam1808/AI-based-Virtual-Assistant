from input_module import take_input
from process_module import process
from output_module import output
import welcome
import os
import assistant_details as ad
from database import listen_is_on
from listen_module import listen
import AssistantGUI as gui
from automatic import check_last_modify

from pathlib import Path
my_file = Path("setup.py")

if my_file.is_file():
	import setup


if ad.is_ubuntu():
	os.system('clear')
else:
	os.system('cls')

def installation():
	f = open("setup.py", "a")
	print("-----------Welcome to Virtual Assistant------------")
	output("Before starting few Setup is required")
	output("Should I Call You Ma'am or Sir or whatever you say")
	status = take_input()
	statement1 = 'status = "' + status + '"' + '\n'
	f.write(statement1)
	output("Do you want to set the path for music")
	ans = take_input()
	if ans.lower() == 'yes':
		output("Enter Path")
		path = take_input()
		statement2 = 'music_path = "' + path + '"' + '\n'
		f.write(statement2)
	else:
		statement2 = 'music_path = "' + '"' + '\n'
		f.write(statement2)
	f.close()


if my_file.is_file():
    #Welcome message
	status = setup.status
	check_last_modify()
	welcome.greet(status)
	while(True):
		if listen_is_on():
			i = listen()
		else:
			i = take_input()
		o = process(i)
		output(o)
else:
	installation()
	import setup
	status = setup.status
	welcome.greet(status)

	while(True):
		if listen_is_on():
			i = listen()
		else:
			i = take_input()
		o = process(i)
		output(o)

