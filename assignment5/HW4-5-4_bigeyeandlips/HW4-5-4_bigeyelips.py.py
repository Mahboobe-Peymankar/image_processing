import numpy as np
import cv2
import tensorflow as tf
from functools import partial
import time
from TFLiteFaceDetector import UltraLightFaceDetecion
from TFLiteFaceAlignment import CoordinateAlignmentModel

def get_mark (pred,  points):
    mark = []
    for i in points:
        mark.append (pred [i])
    mark = np.array (mark, dtype= int)
    
    print (mark)

    return mark 

def zoom (image, mark ) :
    x,y,w,h =cv2.boundingRect (mark)

    result = image [y :y+h , x : x + w]
    result_big =cv2.resize (result , (0,0) , fx=2,fy=2)

    return result_big




lips=[52 , 55, 56, 53, 59,58,61,68,67,71,63,64,65]
eye1=[89,90,87,91,93,96,94,95]
eye2=[39,42,40,41,35,36,33,37]


fd = UltraLightFaceDetecion("assignment5\HW4-5-4_bigeyeandlips\weights\RFB-320.tflite", conf_threshold=0.88)
fa = CoordinateAlignmentModel("assignment5\HW4-5-4_bigeyeandlips\weights\coor_2d106.tflite")


woman= cv2.imread ("assignment5\HW4-5-4_bigeyeandlips\input\woman.jpg")
 
rows, cols ,_= woman.shape


color = (0, 0, 125)

start_time = time.perf_counter()

boxes, scores = fd.inference(woman)

for pred in fa.get_landmarks(woman, boxes):
    lips_mark = get_mark(pred ,lips)
    eye1_mark = get_mark(pred, eye1)
    eye2_mark = get_mark (pred , eye2)



   
mask = np.zeros (woman.shape, dtype= np.uint8)
    

cv2.drawContours (mask , [lips_mark] , -1 , (255,255,255) , -1)
cv2.drawContours (mask , [eye1_mark] , -1 , (255,255,255) , -1)
cv2.drawContours (mask , [eye2_mark] , -1 , (255,255,255) , -1)
mask = mask //255


result = woman * mask

result_big_lips = zoom (result, lips_mark)
result_big_eye1 = zoom (result, eye1_mark)
result_big_eye2 = zoom (result, eye2_mark)

mak = np.zeros (woman.shape, dtype= np.uint8) 

print (result_big_lips.shape,result_big_eye1.shape , result_big_eye2.shape)

mask[50:50 + 16, 90-42 :90  ] = result_big_eye2
mask[50:50 + 16, 100 :100 +38] = result_big_eye1
mask[90:90+ 30,68:68+62] = result_big_lips

x, y, w, h = [0, 0, woman.shape[0], woman.shape[1]]
for i in range(w):
    for j in range(h):
        if mask[i][j][0] == 0 and mask[i][j][1] == 0 and mask[i][j][2] == 0:
            mask[i][j] = woman[i,j]
woman[ x:x+w,y:y+h] = mask



print(time.perf_counter() - start_time)
cv2.imshow("result", woman)
cv2.waitKey()
cv2.imwrite ("assignment5\HW4-5-4_bigeyeandlips/result.jpg",woman)

