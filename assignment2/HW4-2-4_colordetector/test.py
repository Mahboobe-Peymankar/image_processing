
# Python program to explain cv2.blur() method  
  
# importing cv2  
import cv2  
  
# path  

  
# Reading an image in default mode  
image = cv2.imread("assignment2\HW4-2-3_snowfall\winter.jpg")  
image = cv2.resize (image ,(600,400))
image= cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
  
# Window name in which image is displayed  
window_name = 'Image'
  
# ksize 
ksize = (100, 100) 
  
# Using cv2.blur() method  
image = cv2.blur(image, ksize)  
  
# Displaying the image  
cv2.imshow(window_name, image)  

cv2.waitKey ()