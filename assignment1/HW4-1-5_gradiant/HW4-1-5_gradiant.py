import cv2

my_image = cv2.imread("assignment1\HW4-1-5_gradiant\whiteboard.jpg")
print (my_image.shape)



for i in range (229):
    for j in range (296):
        my_image [i , j] = 255- 255 * i /229
        

     


cv2.imshow ("" , my_image)
cv2.waitKey ()

cv2.imwrite ("assignment1\HW4-1-5_gradiant\gradiant.jpg" , my_image)   