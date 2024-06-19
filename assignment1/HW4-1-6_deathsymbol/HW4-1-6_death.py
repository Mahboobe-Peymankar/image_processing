import cv2

my_image = cv2.imread("assignment1\HW4-1-6_deathsymbol/first.jpg")
print (my_image.shape)



for i in range (100):
    my_image [ i , 100 - i  : 100 + 40 - i ] = 0


for i in range (40):
    my_image [100 + i , 0 : 40 - i] = 0
        

     


cv2.imshow ("" , my_image)
cv2.waitKey ()

cv2.imwrite ("assignment1\HW4-1-6_deathsymbol\death.jpg" , my_image)   

