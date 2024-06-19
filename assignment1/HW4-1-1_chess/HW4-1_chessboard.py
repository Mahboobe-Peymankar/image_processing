import cv2

my_image = cv2.imread("assignment1\HW4-1-1_chess\whiteboard.jpg")
print (my_image.shape)

my_image [33:35 , 66 :230] = 0
my_image [33:197 , 66 :68] = 0
my_image [33:197 , 228:230] = 0
my_image [195:197, 66 :230] = 0    
k = 0
for i in range (35, 195, 20):
    
    w = 0
    for j in range (68, 228 , 20):

        if  (k + w ) % 2 == 0 :
            my_image [i : i + 20 , j : j + 20] = 0
        else :
            my_image [i : i + 20 , j : j + 20] = 255
        w += 1
    k += 1

     


cv2.imshow ("" , my_image)
cv2.waitKey ()

cv2.imwrite ("assignment1\HW4-1-1_chess\chess.JPG" , my_image)   