import os
import cv2
import numpy as np

results = []

for f in range (1,len(next(os.walk('assignment4\HW4-4-2_blackhole\input'))[1])+1):
    images_path = os.listdir ("assignment4\HW4-4-2_blackhole\input/" + str (f))
    print (images_path)
    images= []
    
    for image_path in images_path :
        image = cv2.imread ("assignment4\HW4-4-2_blackhole\input/" + str (f) + "/" + image_path)

        image= cv2.cvtColor (image , cv2.COLOR_BGR2GRAY)
        image = image.astype (np.float32)
        images.append(image)

    result = np.zeros (image.shape)

    for image in images :
        result += image

    result = result / len (images)
    result =result.astype (np.uint8)
    
    results.append (result)

combined_image_1 = np.concatenate((results[0] , results[1]) , axis=1 )
combined_image_2 = np.concatenate((results[2], results[3]) ,  axis=1 )
combined_image = np.concatenate((combined_image_1,combined_image_2) , axis=0 )

cv2.imwrite ("assignment4\HW4-4-2_blackhole\combined_images.jpg" , combined_image)
cv2.imshow ("",combined_image)
cv2.waitKey ()
        
