import cv2
import os
import numpy as np

def get_limits(color):
    c = np.uint8([[color]]) # Create numpy array of type uint8 containing the BGR color value
    color_in_HSV = cv2.cvtColor(c, cv2.COLOR_BGR2HSV)
    lower_limit = color_in_HSV[0][0][0] - 10, 100, 100
    upper_limit = color_in_HSV[0][0][0] + 10, 255, 255
    
    lower_limit = np.array(lower_limit, dtype=np.uint8)
    upper_limit = np.array(upper_limit, dtype=np.uint8)
    return lower_limit, upper_limit

