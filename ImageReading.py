#Imports necessary packages
import cv2 as cv

#Creates function for reading images
def readImage(img):
    #Loads the image and returns the loaded image
    image = cv.imread(img)
    return image

