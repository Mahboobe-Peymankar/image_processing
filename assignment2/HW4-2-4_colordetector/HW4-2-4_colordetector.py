import cv2
import imageio

def set_frame(frame):
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    print (frame.shape)
    cv2.rectangle(frame, (200, 100), (400, 250), 0, 4)

    blured_frame = cv2.blur (frame , (60,60))
    
    blured_frame [100 :250, 200:400] = frame[100:250, 200:400]
    return blured_frame



def detect_color(frame):

    no_black_pixcel = 0
    no_white_pixcel = 0
    no_gray_pixcel = 0

    



    for i  in range (100,250,1) :
        for j  in range (200 , 400) :
            if  0<=frame[i][j]<= 25 :
                no_black_pixcel += 1
            elif 81 <= frame [i] [j] <= 180 :
                no_gray_pixcel += 1
            else :
                no_white_pixcel += 1

    array = [no_black_pixcel , no_gray_pixcel , no_white_pixcel]
    print (array)
    max_index = array.index(max(array))
    if max_index == 0 :
        color = "black"
    elif max_index == 1 :
        color = "gray"
    else :
        color = "white"
    print  (color)
    return color





    


   

frames = []
capture = cv2.VideoCapture(0)
while(True):
    _, frame = capture.read()
    preset_frame = set_frame(frame)

    color = detect_color(preset_frame)#[200:300, 100:200])
    cv2.putText(preset_frame, color, (20, 55), cv2.FONT_HERSHEY_PLAIN, 4, 0, 5)
    cv2.imshow('frame', preset_frame)
    frames.append(preset_frame)
    
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break




imageio.mimsave('assignment2\HW4-2-4_colordetector\Color_Detector.gif', frames)