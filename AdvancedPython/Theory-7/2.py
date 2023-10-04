import pyautogui
import time

def automate_keyboard_actions():
#Capture and st the screenshot
    pyautogui.screenshot("ss.png")
    # Simulate typing a text
    pyautogui. write("Hello, PyAutoGUI!", interval=0.2)
    # Simulate pressing the "Ctr1" and "C" keys together (copy)
    pyautogui.hotkey('ctrl','c') #hotkey () function that helps us
    # Type the copied text
    pyautogui.hotkey('ctrl','v')

if name == "main" : 
    time.sleep(5) # Wait for 5 seconds before starting
    automate_keyboard_actions()