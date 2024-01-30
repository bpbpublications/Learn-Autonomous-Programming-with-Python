#The cursor coordinates that have been inserted here are the ones that were obtained during the trial run at arbitrary positions near the search bar
#and search result. Feel free to insert your own coordinates obtained after running the file 'getting cursor positions for use case.py.' 

import pyautogui
import time
pyautogui.click(192, 1058, 2,0,'left')   
pyautogui.typewrite('word')
pyautogui.moveTo(265,377,duration=2)  
pyautogui.click(265, 377, 2,0,'left')  
time.sleep(3)
pyautogui.typewrite('Python use case executed!',0.5)