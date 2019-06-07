#saturday.py: Messages for saturday

import datetime
import sys
import time
import webbrowser

#web url/chrome location/current hour creation
url = 'http://lmgtfy.com/?q=zerg+rush'
chrome_loc = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

now = datetime.datetime.now()
datetime.time(now.hour)

#creating saturday function for string iteration based on hour of day
def saturday_msg():
  msg_list = ["Saturday...",
              "Saturday...",
              "Saturday...",
              "Saturday...",
              "Saturday...",
              "Saturday...",
              "Do you work Saturdays?",
              "Do you work Saturdays?",
              "Do you work Saturdays?",
              "Do you work Saturdays?",
              "Do you work Saturdays?",
              "Do you work Saturdays?",
              "Saturday is for the cats!",
              "Saturday is for the cats!",
              "Saturday is for the cats!",
              "Saturday is for the cats!",
              "Saturday is for the cats!",
              "Saturday is for the cats!",
              "It's Saturday, are you partying?",
              "It's Saturday, are you partying?",
              "It's Saturday, are you partying?",
              "It's Saturday, are you partying?",
              "It's Saturday, are you partying?",
              "It's Saturday, are you partying?"]

  #starts iterating through each character of the message
  msg = iter(msg_list[now.hour])
  sys.stdout.write(next(msg))
  sys.stdout.flush()

  for i in msg:
    time.sleep(0.25)
    sys.stdout.write(i)
    sys.stdout.flush()

def saturday_hldy_msg():
  pass
  #messages for holidays on saturday   
    
saturday_msg()
time.sleep(1.5)

#webbrowser opens to 'let me google that for you'(lmgtfy): zerg rush
#program ends after a few seconds
webbrowser.get(chrome_loc).open_new_tab(url)
sys.exit(0)
