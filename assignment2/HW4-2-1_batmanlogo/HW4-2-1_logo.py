import cv2
image = cv2.imread ("HW4-2-1_batmanlogo\logo.png")

image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

_ , image = cv2.threshold (image , 100 , 255 ,cv2.THRESH_BINARY_INV)

cv2.putText  (image , "BATMAN" , (305 ,480) , cv2.FONT_HERSHEY_COMPLEX_SMALL , 3 , 255)

cv2.imshow ("result", image)

cv2.waitKey()

cv2.imwrite ("HW4-2-1_batmanlogo\logoresult.jpg",image)

