import cv2

my_image_1 = cv2.imread("assignment1\HW4-1-2_invertcolor/first.jpg")
print (my_image_1.shape)


for i in range (645):
    for j in range (645):
        my_image_1 [i , j] = 255 - my_image_1 [i , j]

     

cv2.imshow ("" , my_image_1)
cv2.waitKey ()

cv2.imwrite ("assignment1\HW4-1-2_invertcolor/first_inverted.jpg" , my_image_1)   

my_image_2 = cv2.imread("assignment1\HW4-1-2_invertcolor/second.jpg")
print (my_image_2.shape)


for i in range (1202):
    for j in range (900):
        my_image_2 [i , j] = 255 - my_image_2 [i , j]

     

cv2.imshow ("" , my_image_2)
cv2.waitKey ()

cv2.imwrite ("assignment1\HW4-1-2_invertcolor/second_inverted.jpg" , my_image_2)   