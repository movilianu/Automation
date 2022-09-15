from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.get("https://accounts.google.com/signup")

"""
Make an action to open a new tab - code here
"""

#prints parent window title
print("Parent window title: " + driver.title)

#get current window handle
p = driver.current_window_handle

#get first child window
chwd = driver.window_handles

for w in chwd:
#switch focus to child window
    if(w!=p):
    driver.switch_to.window(w)
break
