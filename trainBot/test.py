import pyautogui as pt
from time import sleep
import pytesseract
from PIL import ImageGrab

speed_left = 1134
speed_top = 1134
speed_right = 1152
speed_bottom = 1152


sleep(2)
#image = ImageGrab.grab(bbox=(speed_left, speed_top, speed_right, speed_bottom))
#image = pt.screenshot(region=(speed_left, speed_top, speed_right, speed_bottom))
#image.save('screenshot.png')
#print("saved screenshot")


import pyautogui

# Get the current mouse position
currentMouseX, currentMouseY = pyautogui.position()

# Print the mouse position
print(f"Mouse position: ({currentMouseX}, {currentMouseY})")