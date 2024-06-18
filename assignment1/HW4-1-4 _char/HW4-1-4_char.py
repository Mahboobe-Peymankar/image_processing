import cv2

my_image = cv2.imread("assignment1\HW4-1-4 _char\whiteboard.jpg")
print (my_image.shape)

my_image [90:140 , 123 :133] = 0
my_image [90:140 , 163 :173] = 0

for i in range (50):
    my_image [90 + i , 4*i // 10 +123 : 4 *i // 10 + 133] = 0
    my_image [90 + i , -4*i // 10 +163 : -4 *i // 10 + 173] = 0

     


cv2.imshow ("" , my_image)
cv2.waitKey ()

cv2.imwrite ("assignment1\HW4-1-4 _char\char.jpg" , my_image)   