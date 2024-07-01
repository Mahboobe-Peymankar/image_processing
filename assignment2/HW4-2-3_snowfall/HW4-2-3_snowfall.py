import cv2
import numpy as np
import imageio

image = cv2.imread ("assignment2\HW4-2-3_snowfall\winter.jpg")

image= cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
image=cv2.resize (image , (600 ,400))
original_image = image




rows , cols = image.shape


frames =[]


while True :
    
    image = cv2.imread ("assignment2\HW4-2-3_snowfall\winter.jpg")

    image= cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image=cv2.resize (image , (600 ,400))

    # image = original_image
    # cv2.imshow ("image" , original_image)

    

    for _ in range (100):
        snow_row = np.random.randint(0,rows-1) 
        snow_col = np.random.randint (0,cols-1)
        snow = cv2.circle ( image ,  (snow_col ,snow_row) , 1, (255 ,255, 255) , -1)
        blended_image = cv2.addWeighted (image , 0.9 , snow , 0.1 , 0)

    
    

    

    

    
    
    frame = blended_image.astype(np.uint8)
    frames.append (frame)
    cv2.imshow  ("snowfall" ,blended_image)
    
   
    
    
    
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break



cv2.imwrite ("assignment2\HW4-2-3_snowfall\snowfall.jpg",frame)
imageio.mimsave ("assignment2\HW4-2-3_snowfall\snowfall.gif",frames)
