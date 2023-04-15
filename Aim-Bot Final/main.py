import cv2
import numpy as np
import mss
import win32api
import win32con
import time



cascade_path = 'G:/Khaled/CSIT/Code/Aim-Bot Final/classifier/cascade.xml'
cascade = cv2.CascadeClassifier(cascade_path)

scale = 1.1
min_neighbors = 3
min_size = (30, 30)
max_size = (100, 100)

mouse_button = win32con.MOUSEEVENTF_LEFTDOWN | win32con.MOUSEEVENTF_LEFTUP
mouse_speed = 10

time.sleep(5)

while True:
    with mss.mss() as sct:
        monitor = {"top":0, "left":0, "width":1920, "height":1080}
        img_array = np.array(sct.grab(monitor))

    gray = cv2.cvtColor(img_array, cv2.COLOR_BGR2GRAY)

    circles = cascade.detectMultiScale(
        gray,
        scaleFactor=scale,
        minNeighbors=min_neighbors,
        minSize=min_size,
        maxSize=max_size
    )

    center = (monitor["width"] // 2, monitor["height"] // 2)
    nearest_circle = None
    min_distance = float('inf')
    for (x, y, w, h) in circles:
        distance = ((x + w // 2) - center[0])**2 + ((y + h // 2) - center[1])**2
        if distance < min_distance:
            nearest_circle = (x, y, w, h)
            min_distance = distance

    if nearest_circle is not None:
        x, y, _, _ = nearest_circle
        print(x,y)
        #win32api.SetCursorPos((x + w // 2, y + h // 2))
        #win32api.mouse_event(mouse_button, 0, 0, 0, 0)
        #win32api.mouse_event(mouse_button, 0, 0, 0, 0)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
