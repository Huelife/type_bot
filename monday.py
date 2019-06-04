#monday.py: Messages for monday

import datetime
import sys
import time
import webbrowser

#web url/chrome location/current hour creation
url = 'http://lmgtfy.com/?q=zerg+rush'
chrome_loc = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

now = datetime.datetime.now()
datetime.time(now.hour)

#creating monday function for string iteration
def monday_msg():
  msg_list = ["Don't be a Monday morning zombie!",
              "Don't be a Monday morning zombie!",
              "Don't be a Monday morning zombie!",
              "Don't be a Monday morning zombie!",
              "Don't be a Monday morning zombie!",
              "Don't be a Monday morning zombie!",
              "Don't be a Monday morning zombie!",
              "Mondays!",
              "Mondays!",
              "Mondays!",
              "Mondays!",
              "Mondays!",
              "Mondays!",
              "So much work on Monday!",
              "So much work on Monday!",
              "So much work on Monday!",
              "So much work on Monday!",
              "So much work on Monday!",
              "Monday cold beers...",
              "Monday cold beers...",
              "Monday cold beers...",
              "Monday cold beers...",
              "Monday cold beers...",
              "Monday cold beers..."]

  msg = iter(msg_list[now.hour])
  sys.stdout.write(next(msg))
  sys.stdout.flush()

  for i in msg:
    time.sleep(0.25)
    sys.stdout.write(i)
    sys.stdout.flush()

def monday_hldy_msg():
  pass
  #messages for holidays on monday    
    
monday_msg()
time.sleep(1.5)

#webbrowser opens to 'let me google that for you'(lmgtfy): zerg rush
#program ends after a few seconds
webbrowser.get(chrome_loc).open_new_tab(url)
sys.exit(0)
