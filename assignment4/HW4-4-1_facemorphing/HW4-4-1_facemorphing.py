import cv2
import numpy as np

image_person1 = cv2.imread ("assignment4\HW4-4-1_facemorphing\input/person_1.jpg")
image_person2 = cv2.imread ("assignment4\HW4-4-1_facemorphing\input/person_2.jpg")
print (image_person1.shape ,image_person2.shape)

image_person1 =cv2.cvtColor (image_person1 , cv2.COLOR_BGR2GRAY)
image_person2 =cv2.cvtColor (image_person2 , cv2.COLOR_BGR2GRAY)



image_person1 = image_person1.astype ("float32")
image_person2 = image_person2.astype ("float32")
results = []

for i in range (5) :
    result = (i * image_person1 + (5-i) *image_person2) / 5
    
    # result_name = str (i) + ".jpg"
    # result_path = "assignment4\HW4-4-1_facemorphing\input/" + result_name
    result = result.astype(np.uint8) 
    results.append(result)
    # cv2.imwrite (result_path , result)

combined_image = np.concatenate((results[0] , results[1] , results[2], results[3], results[4]) ,    axis=1 )
cv2.imwrite ("assignment4\HW4-4-1_facemorphing/combined_images.jpg" , combined_image)
cv2.imshow ("",combined_image)
cv2.waitKey ()