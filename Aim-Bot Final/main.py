import cv2
import numpy as np
import mss

import win32api
import win32con
import ait

path = 'G:/Khaled/CSIT/Code/Aim-Bot Final/classifier/cascade.xml' # cascade path


# cascade values for tweaking
scale = 2 # lower scale = better detection = lower performance
min_neig = 4 # lower minimum neighbour = more detection (might be false detection)

cascade = cv2.CascadeClassifier(path)


while True:
    a = win32api.GetKeyState(0x26)  # up arrow key
    if a < 0:
        break

while True:
    with mss.mss() as sct:
        monitor = {"top":0, "left":0, "width":1920, "height":1080}
        img_array = np.array(sct.grab(monitor))

    gray = cv2.cvtColor(img_array, cv2.COLOR_RGB2GRAY)
    detection = cascade.detectMultiScale(gray, scale, min_neig)
    
    for (x, y, w, h) in detection:
        print(x, y, w, h)
        

    
    a = win32api.GetKeyState(0x28)  # down arrow key
    if a < 0:
        break