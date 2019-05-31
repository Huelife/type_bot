#saturday.py: Messages for saturday

import datetime
import sys
import time
import webbrowser

url = 'http://lmgtfy.com/?q=zerg+rush'
chrome_loc = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

now = datetime.datetime.now()
datetime.time(now.hour)

def saturday_msg():
  msg_list = ["a0",
              "a1",
              "a2",
              "a3",
              "a4",
              "a5",
              "a6",
              "a7",
              "a8",
              "a9",
              "a10",
              "a11",
              "a12",
              "a13",
              "a14",
              "a15",
              "a16",
              "a17",
              "a18",
              "a19",
              "a20",
              "a21",
              "a22",
              "a23"]

  msg = iter(msg_list[now.hour])
  sys.stdout.write(next(msg))
  sys.stdout.flush()

  for i in msg:
    time.sleep(0.25)
    sys.stdout.write(i)
    sys.stdout.flush()
    
saturday_msg()
time.sleep(1.5)

#webbrowser opens to 'let me google that for you'(lmgtfy): zerg rush
#program ends after a few seconds
webbrowser.get(chrome_loc).open_new_tab(url)
sys.exit(0)
