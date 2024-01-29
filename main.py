#Imports necessary packages
import ImageReading
import ImageProcessing
import ImageDisplaying

#Loads the image
file = "sodaCan.jpg"
circle = ImageReading.readImage(file)

#Applies image detection
ImageProcessing.processImage(circle)

#Displays image with hough lines
ImageDisplaying.displayImage(circle)

