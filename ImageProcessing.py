#Imports necessary packages
import cv2 as cv
import numpy as np

def processImage(image):
    #Applies gaussian blur and canny edge detection on image
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    gray_scale = cv.GaussianBlur(gray, (15, 15),0)
    canny_image = cv.Canny(gray_scale, 100, 120)

    #Creates hough lines around image
    circle = cv.HoughCircles(canny_image, cv.HOUGH_GRADIENT, 145, 400,
                              param1 = 50, param2 = 30,
                              minRadius = 150, maxRadius = 205)

    #Creates array of points around the circle using the hough lines
    circle_arr = np.uint16(np.round(circle))

    for point in circle_arr[0, :]:
        #Creates the circle around the image
        cv.circle(image, (point[0] + 5, point[1] - 14), point[2] + 15, (0, 255, 0), 5)

        #Finds the center point of the circle
        cv.circle(image, (point[0] + 5, point[1] - 14), 2, (0, 0, 255), 5)




