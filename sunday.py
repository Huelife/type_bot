#sunday.py: Messages for sunday

import datetime
import sys
import time
import webbrowser

#web url/chrome location/current hour creation
url = 'http://lmgtfy.com/?q=zerg+rush'
chrome_loc = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

now = datetime.datetime.now()
datetime.time(now.hour)

#creating sunday function for string iteration
def sunday_msg():
  msg_list = ["Go to sleep, it's Sunday...",
              "Go to sleep, it's Sunday...",
              "Go to sleep, it's Sunday...",
              "Go to sleep, it's Sunday...",
              "Go to sleep, it's Sunday...",
              "Go to sleep, it's Sunday...",
              "Go to sleep, it's Sunday...",
              "It's a lazy Sunday morning...",
              "It's a lazy Sunday morning...",
              "It's a lazy Sunday morning...",
              "It's a lazy Sunday morning...",
              "It's a lazy Sunday morning...",
              "Sunday funday!",
              "Sunday funday!",
              "Sunday funday!",
              "Sunday funday!",
              "Sunday funday!",
              "Sunday funday!",
              "Sunday evenings before work...",
              "Sunday evenings before work...",
              "Sunday evenings before work...",
              "Sunday evenings before work...",
              "Sunday evenings before work...",
              "Sunday evenings before work..."]

  msg = iter(msg_list[now.hour])
  sys.stdout.write(next(msg))
  sys.stdout.flush()

  for i in msg:
    time.sleep(0.25)
    sys.stdout.write(i)
    sys.stdout.flush()

def sunday_hldy_msg():
  pass
  #messages for holidays on sunday   
    
sunday_msg()
time.sleep(1.5)

#webbrowser opens to 'let me google that for you'(lmgtfy): zerg rush
#program ends after a few seconds
webbrowser.get(chrome_loc).open_new_tab(url)
sys.exit(0)
