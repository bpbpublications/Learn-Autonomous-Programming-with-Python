

import pyautogui
import xlwings as xw
import time

objWorkbook = xw.Book()
objWorkbook.activate(steal_focus=True)

time.sleep(3)

pyautogui.typewrite('Hello World!',0.5) 
 
pyautogui.hotkey('enter')  
pyautogui.hotkey('up')
pyautogui.hotkey('ctrl','x')
pyautogui.hotkey('down')
pyautogui.hotkey('ctrl','v')
pyautogui.hotkey('esc')

