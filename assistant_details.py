from database import get_name
import os
from sys import platform

name = get_name()


def is_ubuntu():
	if platform == 'linux':
		return True
	elif platform == 'win32':
		return False
