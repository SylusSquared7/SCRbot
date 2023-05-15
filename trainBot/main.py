import pyautogui as pt
from time import sleep
import pytesseract
from PIL import ImageGrab
import cv2
import pytesseract
import numpy as np

current_speed = 0
max_speed = 0
target_speed = 0.0
duration = 1000
throttle_points = 0
distance_to_station = 0

dist_left = 993
dist_top = 1157
dist_right = 500
dist_bottom = 500

speed_left = 988
speed_top = 1134
speed_width = 20
speed_height = 19



# Helper function
def nav_to_image(image, clicks, off_x=0, off_y=0):
    position = pt.locateCenterOnScreen(image, confidence=.7)


    if position is None:
        print(f'{image} not found..')
        return 0
    else:
        pt.moveTo(position, duration=.1)
        pt.moveRel(off_x,off_y, duration=.1)
        pt.click(clicks=clicks, interval=.3)

# Moves the character

# w = move

# s = brake

def get_speed():
    image = cv2.cvtColor(np.array(ImageGrab.grab(bbox=(speed_left, speed_top, speed_left+speed_width, speed_top+speed_height))), cv2.COLOR_RGB2GRAY)
  #  image = cv2.imread(image1, 0)
    thresh = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    speed = pytesseract.image_to_string(thresh, lang='eng',config='--psm 6')
    current_speed = speed
    return speed



def move_character(key_press, duration, action='stopped'):
    pt.keyDown(key_press)
    if action == 'stopped':
        print("stopping")
        pt.keyDown('s')
    elif action == 'drive':
        pt.keyDown('w')
        print("Throttle up for: ", duration, " seconds")

    sleep(duration)
    pt.keyUp(key_press)

def locate_red():
    position = pt.locateCenterOnScreen("images/redSignal.png", confidence=.9)

    if position is None:
        return False
    else:
        print("RED SIGNAL!")
        return True
    
def locate_yellow():
    position = pt.locateCenterOnScreen("images/yellowSignal.png", confidence=.9)

    if position is None:
        return False
    else:
        print("Yellow signal")
        return True
    
def aws_check():
    position = pt.locateCenterOnScreen("images/warning.png", confidence=.9)

    if position is None:
        return False
    else:
        print("AWS recognised")
        pt.keyDown('q')
        sleep(0.2)
        pt.keyUp('q')
        print("AWS delt with")
    
def locate_station():
    position = pt.locateCenterOnScreen("images/stopToLoadPassengers.png", confidence=.7)

    if position is None:
        return False
    else:
        print("Need to stowp at station")
        return True

def get_to_speed():
    while current_speed != target_speed:
        get_speed()
        if target_speed > current_speed:
            pt.keyDown('w')
            sleep(0.25)
            pt.keyUp('w')  
            throttle_points += 0.25
        elif target_speed < current_speed:
            pt.keyDown('s')
            sleep(0.25)
            pt.keyUp('s')  
        #    throttle_points -= 0.25
        else:
            print("Target speed reached")


# start the program
sleep(5)
print("Program started")
while duration != 0:
    aws_check()
    if locate_station():
        target_speed = 15
        get_to_speed()
        sleep(8)
        target_speed = 0
        get_to_speed()        

    if not locate_red():
        target_speed = 25
        if target_speed == current_speed:
            print("Current speed matches target speed")
        elif target_speed > current_speed:
            if throttle_points == 100:
                print("Throttle is full cannot drive faster")
            else:
                get_to_speed()    
    else:
        print("Signal ahead is red, train is stopped")
        move_character('s', 4, 'stopped')
duration -= 1

