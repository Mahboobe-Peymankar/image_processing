import cv2
import numpy as np
from TFLiteFaceDetector import UltraLightFaceDetecion
from TFLiteFaceAlignment import CoordinateAlignmentModel

lips=[52 , 55, 56, 53, 59,58,61,68,67,71,63,64,65]
eye1=[89,90,87,91,93,96,94,95]
eye2=[35,42,40,41,39,36,33,37]


def rotate(landmarks, coordinates, offset_divide, resize_value):
    result = crop_body_part(landmarks, img)
    result_cw_180 = cv2.rotate(result, cv2.ROTATE_180)
    result_cw_180 = cv2.resize(result_cw_180, (0, 0), fx=resize_value, fy=resize_value)
    w, h, _ = result_cw_180.shape
    gray = cv2.cvtColor(result_cw_180, cv2.COLOR_BGR2GRAY)
    _, mask = cv2.threshold(gray, 1, 255, cv2.THRESH_BINARY)
    not_mask = cv2.bitwise_not(mask)
    mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
    not_mask = cv2.cvtColor(not_mask, cv2.COLOR_GRAY2BGR)
    mask = mask // 255
    not_mask = not_mask // 255
    start_x = int(coordinates[1])-w//2
    if offset_divide != 0:
        start_x -= w//offset_divide
    end_x = start_x + w
    start_y = int(coordinates[0])
    end_y = start_y + h
    img[start_x:end_x, start_y:end_y] = mask * result_cw_180 + not_mask * img[start_x:end_x, start_y:end_y]

def get_mark (pred,  points):
    mark = []
    for i in points:
        mark.append (pred [i])
    mark = np.array (mark, dtype= int)
    
    

    return mark 

def crop_body_part(landmarks, img):
    mask = np.zeros(img.shape, dtype = np.uint8)
    cv2.drawContours(mask, [landmarks], -1, (255, 255, 255), -1)
    mask = mask//255
    result = img * mask
    x, y, w, h = cv2.boundingRect(landmarks)
    return result [ y : y + h , x : x + w]

fd = UltraLightFaceDetecion("assignment5\HW4-5-2_rotate\weights\RFB-320.tflite", conf_threshold=0.88)
fa = CoordinateAlignmentModel("assignment5\HW4-5-2_rotate\weights\coor_2d106.tflite")
img = cv2.imread("assignment5\HW4-5-2_rotate\input/1.jpg")
color = (0, 0, 255)
boxes, scores = fd.inference(img)
for pred in fa.get_landmarks(img, boxes):

    
    lips_mark = get_mark(pred ,lips)
    eye1_mark = get_mark(pred, eye1)
    eye2_mark = get_mark (pred , eye2)

    
    rotate(lips_mark, pred[52], 0, 1.19)
    rotate(eye1_mark, pred[35], 0, 1.08)
    rotate(eye2_mark, pred[89], 6, 1.09)

cv2.imwrite("assignment5\HW4-5-2_rotate/result.jpg", img = cv2.rotate(img, cv2.ROTATE_180))