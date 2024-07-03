import cv2
import numpy  as np

height = 600
width = 400

football_pitch_image = np.ones ((width,height),dtype= np.uint8) * 140

football_pitch_image [ : , 0 : 20] = 120
football_pitch_image [ : , height-20 : height] = 120

for i in range ( 7 ) :
    if i % 2 != 0 :
        football_pitch_image [ : , 20 + i * (height - 40) // 7 : 20 + (i+1) * (height - 40) // 7 ] = 120

cv2.rectangle (football_pitch_image , (20,20) , (height -20 ,width- 20) , 255 , 2)
cv2.rectangle (football_pitch_image , (20, width//2 - (width-40)//8) , (20 +(width-40)//8  ,  width //2 + (width-40)//8 ) , 255 , 2)
cv2.rectangle (football_pitch_image , (20, width//2 - (width-40)//4) , (20 +(width-40)//4  ,  width //2 + (width-40)//4 ) , 255 , 2)

cv2.rectangle (football_pitch_image , (height - 20 -(width-40)//8 , width//2 - (width-40)//8) , (height - 20  ,  width //2 + (width-40)//8 ) , 255 , 2)
cv2.rectangle (football_pitch_image , (height -20 -(width-40)//4 , width//2 - (width-40)//4) , ( height -20,  width //2 + (width-40)//4 ) , 255 , 2)


cv2.line (football_pitch_image , (height //2,20) , (height//2,width - 20) , 255 , 2)

cv2.circle (football_pitch_image , (height // 2 , width // 2) , 4 , 255 , -1)
cv2.circle (football_pitch_image , (height // 2 , width // 2) , (width - 40 ) // 6 , 255  , 2)



cv2.imshow ("result",football_pitch_image)
cv2.waitKey ()
cv2.imwrite ( "assignment3\HW4-3-1_footballpitch/football_pitch.jpg", football_pitch_image)
