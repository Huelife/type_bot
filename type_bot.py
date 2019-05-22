#type bot:
import time
import datetime
import webbrowser
import sys

now = datetime.datetime.now()
datetime.time(now.hour)
now_hr = now.hour

url = 'http://lmgtfy.com/?q=zerg+rush'
chrome_loc = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

#type certain things depending on hour of day
def msg_type(): 
  if now_hr >= 0 and now_hr < 1:
    msg = iter("Don't look under your bed...")
  elif now_hr >= 1 and now_hr < 6:
    msg = iter("Have fun in your dreams...")
  elif now_hr >= 6 and now_hr < 12:
    msg = iter("WHY AM I INSIDE THIS COMPUTER!?")
  elif now_hr >= 12 and now_hr < 18:
    msg = iter("HELP! I'M STUCK INSIDE!!")
  elif now_hr >= 18 and now_hr < 24:
    msg = iter("Don't turn on the lights...")
  else:
    msg = iter("WE'RE SINKING!!")
    
  sys.stdout.write(next(msg))
  sys.stdout.flush()

  for i in msg:
    time.sleep(0.25)
    sys.stdout.write(i)
    sys.stdout.flush()
  
time.sleep(1.5) #1.5 secs after init, start typing
msg_type()#1 character slowly
time.sleep(1.5) #1.5 secs after typing, open chrome

#webbrowser opens to 'let me google that for you'(lmgtfy): zerg rush
webbrowser.get(chrome_loc).open_new_tab(url)

#program ends after a few seconds
sys.exit(0)
