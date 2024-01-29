#Imports necessary packages
import cv2 as cv
import numpy as np
def displayImage(image):
    #Creates a numpy array for the processed image
    np_image = np.copy(image)
    #Returns the processed image
    cv.imshow("circleWithDetection", np_image)
    cv.waitKey(0)
