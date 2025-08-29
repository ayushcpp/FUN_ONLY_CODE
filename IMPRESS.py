import pyautogui
import time 
time.sleep(5)
count=0
while count<1:
    pyautogui.typewrite("dekh ye ")
    pyautogui.press("enter")
    pyautogui.typewrite("mai type nhi kr rha hun ")
    pyautogui.press("enter")
    pyautogui.typewrite("pr apne aap ho rha")
    pyautogui.press("enter")
    count+=1
