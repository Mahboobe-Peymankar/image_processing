import cv2

my_image = cv2.imread("assignment1\HW4-1-6_deathsymbol\whiteboard.jpg")
print (my_image.shape)



for i in range (30):
    my_image [ i , 30 - i  : 30 + 10 - i ] = 0


for i in range (10):
    my_image [30 + i , 0 : 10 - i] = 0
        

     


cv2.imshow ("" , my_image)
cv2.waitKey ()

cv2.imwrite ("assignment1\HW4-1-6_deathsymbol\death.jpg" , my_image)   

