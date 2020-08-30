import os
import sys
from time_details import get_date
from datetime import datetime, date
import re
 
import assistant_details as ad

def get_time():

	now = datetime.now()
	current_time = now.strftime("%H-%M")
	return current_time

def remind(msg, date, time):

    reminder_time = time[0].split(':')
    current_time = get_time().split('-')

    today_date = get_date().split('-')
    months = ['jan', 'feb', 'march', 'april', 'may', 'june', 'july', 'aug', 'sep', 'oct', 'nov', 'dec']

    reminder_date = date.split(' ')
    # print(today_date[1])
    # print(months.index(reminder_date[1].lower())+1)
    if int(today_date[1]) == months.index(reminder_date[1].lower())+1:
        if reminder_time[0] == current_time[0] and reminder_time[1]==current_time[1]:
            remind_msg = 'notify-send "' + msg + '"'
            if ad.is_ubuntu():
                os.system(remind_msg)
            else:
                from win10toast import ToastNotifier
                toaster = ToastNotifier()
                toaster.show_toast("Virtual Assistant", msg)

            return True
        
    return False

def reminder_set(s):
    # s = "Remind me to call Shivam at 10:00 on 21 July"
    ind1 = s.index('to')
    ind2 = re.search(r"at \d+:\d+", s)

    time = re.findall(r'\d+:\d+', s)
    msg = s[ind1+3:ind2.span()[0]]

    day = re.search(r'on \d+', s).span()[0]
    day_date = s[day+3:]

    return remind(msg, day_date, time)

def reminder_start(s):
    
    while True:
        status = reminder_set(s)
        if status:
            break

reminder_start(sys.argv[1])
