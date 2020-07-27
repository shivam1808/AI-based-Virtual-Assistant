import os
import random
import assistant_details as ad

def change_wallpaper():

	if ad.is_ubuntu():
		wallpaper_path = '/home/shivam-gupta/Pictures/Wallpapers'
		wallpapers = os.listdir(wallpaper_path)
		#os.system("export GIO_EXTRA_MODULES=/usr/lib/x86_64-linux-gnu/gio/modules/")
		wallpaper = random.choice(wallpapers)
		command = 'export GIO_EXTRA_MODULES=/usr/lib/x86_64-linux-gnu/gio/modules/'+'\n'+'gsettings set org.gnome.desktop.background picture-uri file:///'+wallpaper_path+"/"+wallpaper
		os.system(command)
		return "Wallpaper changed"
	else:
		import ctypes
		SPI_SETDESKWALLPAPER = 20 
		ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, 'C:\\Users\\shiva\\Desktop\\AI_Virtual_Assistant\\image.jpg', 0)
		return "Wallpaper changed"





