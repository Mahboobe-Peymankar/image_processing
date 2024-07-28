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
    
    # print (mark)

    return mark 



def rotate_align_face(image, lips, right_eye, left_eye):
    
    left_eye_center = np.mean(left_eye, axis=0).astype(int)
    right_eye_center = np.mean(right_eye, axis=0).astype(int)

    # print (left_eye_center,right_eye_center)

    dy = right_eye_center[1] - left_eye_center[1]
    dx = right_eye_center[0] - left_eye_center[0]

    angle = np.degrees(np.arctan2(dy, dx)) - 180
    eyes_center = (int(right_eye_center[0]), int(right_eye_center[1]))

    rotation_matrix = cv2.getRotationMatrix2D(eyes_center, angle, scale=1)
    aligned_image = cv2.warpAffine(image, rotation_matrix, (image.shape[1], image.shape[0]), flags=cv2.INTER_CUBIC)
    return aligned_image





lips=[52 , 55, 56, 53, 59,58,61,68,67,71,63,64,65]
eye_left=[89,90,87,91,93,96,94,95]
eye_right=[39,42,40,41,35,36,33,37]


fd = UltraLightFaceDetecion("assignment5\HW4-5-3_align\weights\RFB-320.tflite", conf_threshold=0.88)
fa = CoordinateAlignmentModel("assignment5\HW4-5-3_align\weights\coor_2d106.tflite")


image= cv2.imread ("assignment5\HW4-5-3_align\input\mrbean.jpg")
 
rows, cols ,_= image.shape

color = (0, 0, 125)

start_time = time.perf_counter()

boxes, scores = fd.inference(image)

for pred in fa.get_landmarks(image, boxes):
   
    lips_mark = get_mark(pred ,lips)
    eye_left_mark = get_mark(pred, eye_left)
    eye_right_mark = get_mark (pred , eye_right)


result_image = rotate_align_face(image, lips_mark, eye_right_mark, eye_left_mark)

   



print(time.perf_counter() - start_time)
cv2.imshow("result", result_image)
cv2.waitKey()
cv2.imwrite ("assignment5\HW4-5-3_align/result.jpg",result_image)

