# we would need to scope it to a certain window
# could we eliminate the keystroke so it is silent
# run in a background

import pyautogui
import time
pyautogui.FAILSAFE = True
time.sleep(5)
f = open("/usr/share/wordlists/rockyou.txt", 'r')
for word in f:
    pyautogui.typewrite("./fp")
    pyautogui.press('enter')
    pyautogui.typewrite(word)
    pyautogui.press('enter')  # press the Enter key
