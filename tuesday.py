#tuesday.py: Messages for tuesday

import datetime
import sys
import time
import webbrowser

#web url/chrome browser location/current hour creation
url = 'http://lmgtfy.com/?q=zerg+rush'
chrome_loc = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

now = datetime.datetime.now()
datetime.time(now.hour)

#creating tuesday function for string iteration based on hour of day
def tuesday_msg():
  msg_list = ["Atleast Tuesday isn't Monday...",
              "Atleast Tuesday isn't Monday...",
              "Atleast Tuesday isn't Monday...",
              "Atleast Tuesday isn't Monday...",
              "Atleast Tuesday isn't Monday...",
              "Atleast Tuesday isn't Monday...",
              "Tuesday workflow!",
              "Tuesday workflow!",
              "Tuesday workflow!",
              "Tuesday workflow!",
              "Tuesday workflow!",
              "It's taco Tuesday!",
              "It's taco Tuesday!",
              "It's taco Tuesday!",
              "It's taco Tuesday!",
              "It's taco Tuesday!",
              "It's taco Tuesday!",
              "It's taco Tuesday!",
              "Tuesday nights!",
              "Tuesday nights!",
              "Tuesday nights!",
              "Tuesday nights!",
              "Tuesday nights!",
              "Tuesday nights!"]

  #starts iterating through each character of the message
  msg = iter(msg_list[now.hour])
  sys.stdout.write(next(msg))
  sys.stdout.flush()

  for i in msg:
    time.sleep(0.25)
    sys.stdout.write(i)
    sys.stdout.flush()

def tuesday_hldy_msg():
  pass
  #messages for holidays on tuesday   
    
tuesday_msg()
time.sleep(1.5)

#webbrowser opens to 'let me google that for you'(lmgtfy): zerg rush
#program ends after a few seconds
webbrowser.get(chrome_loc).open_new_tab(url)
sys.exit(0)
