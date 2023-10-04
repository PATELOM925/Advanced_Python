"""
drag mouse and click using moveTo and click print screen size
Messagebox usage to generate alert
"""
from pyautogui import *
import pyautogui
import time

def automate_mouse_actions():
    #move the mouse to coordinate (500,500)
    pyautogui.moveTo(500, 500, duration=1)

    #simulate a left mouse button click
    pyautogui.click()

    #move the mouse to coordinates (800,300) and click
    pyautogui.moveTo(800, 300, duration=1)
    #pyautogui.click()


if _name_ == "__main__":
    time.sleep(5)   #wait for 5 sec before starting
    automate_mouse_actions()

    #return monitor screen size
    screenWidth, screenHeight = pyautogui.size()
    print("The screen width is: ", screenWidth)
    print("The screen height is: ", screenHeight)
    #Messagebox with alert() to display message box with some text message and OK button
    pyautogui.alert(text='python_Alert', title='Advanced Python Programming', button="OK")