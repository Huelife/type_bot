#wednesday.py: Messages for wednesday

import datetime
import sys
import time
import webbrowser

#web url/chrome browser location/current hour creation
url = 'http://lmgtfy.com/?q=zerg+rush'
chrome_loc = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

now = datetime.datetime.now()
datetime.time(now.hour)

#creating wednesday function for string iteration based on hour of day
def wednesday_msg():
  msg_list = ["Wednesday mornings are cold...",
              "Wednesday mornings are cold...",
              "Wednesday mornings are cold...",
              "Wednesday mornings are cold...",
              "Wednesday mornings are cold...",
              "Wednesday mornings are cold...",
              "Wednesday workflow!",
              "Wednesday workflow!",
              "Wednesday workflow!",
              "Wednesday workflow!",
              "Wednesday workflow!",
              "Wednesday workflow!",
              "Wednesday is halfwway to the weekend!",
              "Wednesday is halfwway to the weekend!",
              "Wednesday is halfwway to the weekend!",
              "Wednesday is halfwway to the weekend!",
              "Wednesday is halfwway to the weekend!",
              "Wednesday is halfwway to the weekend!",
              "Wednesday evening lullaby...",
              "Wednesday evening lullaby...",
              "Wednesday evening lullaby...",
              "Wednesday evening lullaby...",
              "Wednesday evening lullaby...",
              "Wednesday evening lullaby..."]

  #starts iterating through each character of the message
  msg = iter(msg_list[now.hour])
  sys.stdout.write(next(msg))
  sys.stdout.flush()

  for i in msg:
    time.sleep(0.25)
    sys.stdout.write(i)
    sys.stdout.flush()
 
def wednesday_hldy_msg():
  pass
  #messages for holidays on wednesday

wednesday_msg()
time.sleep(1.5)

#webbrowser opens to 'let me google that for you'(lmgtfy): zerg rush
#program ends after a few seconds
webbrowser.get(chrome_loc).open_new_tab(url)
sys.exit(0)
