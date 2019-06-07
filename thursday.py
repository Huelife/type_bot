#thursday.py: Messages for thursday

import datetime
import sys
import time
import webbrowser

#web url/chrome browser location/current hour creation
url = 'http://lmgtfy.com/?q=zerg+rush'
chrome_loc = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

now = datetime.datetime.now()
datetime.time(now.hour)

#creating thursday function for string iteration based on hour of day
def thursday_msg():
  msg_list = ["Thursday mornings...",
              "Thursday mornings...",
              "Thursday mornings...",
              "Thursday mornings...",
              "Thursday mornings...",
              "Thursday mornings...",
              "Thursday mornings...",
              "Thursday is the new Friday!",
              "Thursday is the new Friday!",
              "Thursday is the new Friday!",
              "Thursday is the new Friday!",
              "Thursday is the new Friday!",
              "Thursday is the new Friday!",
              "Thursday is the new Friday!",
              "Thursday traffic is so bad!",
              "Thursday traffic is so bad!",
              "Thursday traffic is so bad!",
              "Thursday traffic is so bad!",
              "Thursday traffic is so bad!",
              "Thursday is Latin night!",
              "Thursday is Latin night!",
              "Thursday is Latin night!",
              "Thursday is Latin night!",
              "Thursday is Latin night!"]

  #starts iterating through each character of the message
  msg = iter(msg_list[now.hour])
  sys.stdout.write(next(msg))
  sys.stdout.flush()

  for i in msg:
    time.sleep(0.25)
    sys.stdout.write(i)
    sys.stdout.flush()

def thursday_hldy_msg():
  pass
  #messages for holidays on thursday   
    
thursday_msg()
time.sleep(1.5)

#webbrowser opens to 'let me google that for you'(lmgtfy): zerg rush
#program ends after a few seconds
webbrowser.get(chrome_loc).open_new_tab(url)
sys.exit(0)
