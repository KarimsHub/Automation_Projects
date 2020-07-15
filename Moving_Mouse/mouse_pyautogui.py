import pyautogui
import schedule
import time


#currentMouseX, currentMouseY = pyautogui.position() # Get the XY position of the mouse.
#print(currentMouseX, currentMouseY)
def click_function():
    pyautogui.moveTo(3226, 55,duration=2) #insert the x and y coordinates you like
    pyautogui.click() #left click
    pyautogui.moveTo(2226, 55,duration=2)

schedule.every(10).seconds.do(click_function)

while True:
    schedule.run_pending()
    time.sleep(1)