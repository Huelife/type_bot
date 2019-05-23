#type bot:
import time
import webbrowser
import sys

url = 'http://lmgtfy.com/?q=zerg+rush'
chrome_loc = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
 
#wait 1.5 sec, print message, and wait 1.5 sec
time.sleep(1.5)
import msg.py
time.sleep(1.5)

#webbrowser opens to 'let me google that for you'(lmgtfy): zerg rush
#program ends after a few seconds
webbrowser.get(chrome_loc).open_new_tab(url)
sys.exit(0)
