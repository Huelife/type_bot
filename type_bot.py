#type bot:
import time
import datetime
import webbrowser
import sys

now = datetime.datetime.now()
datetime.time(now.minute,now.hour,now.day)
now_min = now.minute
now_hr = now.hour
now_day = now.day
now_mnth = 0
now_yr = 0

url = 'http://lmgtfy.com/?q=zerg+rush'

chrome_loc = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

#type certain things depending on min of day
#type certain things depending on hour of day
#type certain things depending on month of day
#type certain things depending on year of day
def msg_type():
  msg = "Cheeese"
  print(msg)
  if now_min == 9:
    msg = "oh"
  elif now_hr == 12:
    msg = "hi"
  elif now_day == 12:
    msg = "yuh"
  elif now_mnth == 12:
    msg = "there"
  elif now_yr == 2020:
    msg = "buddy"
  else:
    msg = "ERROR!"

time.sleep(1.5) #1.5 secs after init, starts typing

msg_type() #1 character slowly

time.sleep(5) #5 seconds

#webbrowser opens to let me google that for you: zerg rush
webbrowser.get(chrome_loc).open_new_tab(url)

#program ends after 6.5 seconds
sys.exit(0)
