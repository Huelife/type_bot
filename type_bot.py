#type bot.py:

import datetime
import sys
import time
#import webbrowser

#url = 'http://lmgtfy.com/?q=zerg+rush'
#chrome_loc = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

now = datetime.datetime.now()
datetime.time(now.hour)
day_num = int(now.strftime('%w'))

def msg_day():
  if day_num == 0:
    import sunday.py
  elif day_num == 1:
    import monday.py
  elif day_num == 2:
    import tuesday.py
  elif day_num == 3:
    import wednesday.py
  elif day_num == 4:
    import thursday.py
  elif day_num == 5:
    import friday.py
  elif day_num == 6:
    import saturday.py
  else:
    sys.exit(0)

#type certain things depending on hour of day
def msg_type(): 
  if now.hour >= 0 and now.hour < 1:
    msg = iter("Don't look under your bed...")
  elif now.hour >= 1 and now.hour < 6:
    msg = iter("Have fun in your dreams...")
  elif now.hour >= 6 and now.hour < 12:
    msg = iter("WHY AM I INSIDE THIS COMPUTER!?")
  elif now.hour >= 12 and now.hour < 18:
    msg = iter("HELP! I'M STUCK INSIDE!!")
  elif now.hour >= 18 and now.hour < 24:
    msg = iter("Don't turn on the lights...")
  else:
    msg = iter("WE'RE SINKING!!")

#starts iterating through each character of the message
  sys.stdout.write(next(msg))
  sys.stdout.flush()

  for i in msg:
    time.sleep(0.25)
    sys.stdout.write(i)
    sys.stdout.flush()
    
#def msg_type()
#def msg_day()
time.sleep(1.5)

#webbrowser opens to 'let me google that for you'(lmgtfy): zerg rush
#program ends after a few seconds
#webbrowser.get(chrome_loc).open_new_tab(url)
sys.exit(0)
