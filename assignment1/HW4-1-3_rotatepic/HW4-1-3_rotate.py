import cv2

my_image_1 = cv2.imread("assignment1\HW4-1-3_rotatepic/3.jpg")


rotate_shape = cv2.rotate ( my_image_1 , cv2.ROTATE_180)

cv2.imshow ("" , rotate_shape)
cv2.waitKey ()

cv2.imwrite ("assignment1\HW4-1-3_rotatepic/3rotated.jpg" , rotate_shape)   