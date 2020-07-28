import assistant_details
from speak_module import speak
from database import speak_is_on
from colorama import Fore

def output(o):
	#command line output

	print(Fore.RED + assistant_details.name + ": " + o + Fore.RESET)
	
	if speak_is_on():
		speak(o)
	print()