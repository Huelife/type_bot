#type bot:
import time
import datetime
import webbrowser

url = 'http://lmgtfy.com/?q=zerg+rush'

chrome_loc = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

def msg_type():
  msg = " "
  print(msg)
  if now_min == # :
    msg = " "
  elif now_hr == # :
    msg = " "
  elif now_day == # :
    msg = " "
  elif now_mnth == # :
    msg = " "
  elif now_yr == # :
    msg = " "
  else:
    msg = "ERROR!"
#type certain things depending on min of day
#type certain things depending on hour of day
#type certain things depending on month of day
#type certain things depending on year of day

time.sleep(5) #5 secs after init, starts typing

msg_type() #1 character slowwly

time.sleep(30) #30 seconds

#webbrowser opens to google with type words
webbrowser.get(chrome_loc).open_new_tab(url)
#program ends after 30 seconds


