#messages based on hour
  #messages based on minutes
    #messages based on seconds
    
import datetime
import sys
import time

now = datetime.datetime.now()
datetime.time(now.hour)

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
    
def msg_type()
