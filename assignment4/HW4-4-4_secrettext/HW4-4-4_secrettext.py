import cv2
import numpy as np

image_1 = cv2.imread ("assignment4\HW4-4-4_secrettext\input\image.png")
image_2 = cv2.imread ("assignment4\HW4-4-4_secrettext\input/text1.png")
image_1 = cv2.cvtColor (image_1 ,cv2.COLOR_BGR2GRAY)
image_2= cv2.cvtColor (image_2 ,cv2.COLOR_BGR2GRAY)

# result = image_1-image_2
result = cv2.subtract (image_1,image_2)
result = 255-result
cv2.imwrite ("assignment4\HW4-4-4_secrettext/result.png",result)

cv2.imshow ("result" , result)
cv2.waitKey ()