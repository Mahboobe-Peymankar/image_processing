import cv2
import numpy as np
import imageio

image = cv2.imread ("assignment2\HW4-2-2_tvnoise/tv.jpg")

image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
print (image.shape)
rows , cols = image.shape

cv2.rectangle (image , (30,30), (180,148),255,2)
frames =[]
# writer = cv2.VideoWriter("assignment2\HW4-2-2_tvnoise/noise.mp4",cv2.VideoWriter_fourcc (*'mp4v'), 30, (cols , rows))


while True :
    noise = np.random.random( (118,150)) *255
    noise = np.array (noise , dtype= np.uint8)

    image [30:148 , 30:180] = noise
    frame = image.astype(np.uint8)
    frames.append (frame)
    cv2.imshow  ("result" ,image)
   
    # writer.write(frame)
    
    
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break


cv2.imwrite ("assignment2\HW4-2-2_tvnoise/noise.jpg",frame)


imageio.mimsave ("assignment2\HW4-2-2_tvnoise/noise.gif",frames)
# writer.release()