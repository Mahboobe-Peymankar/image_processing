import cv2

def non_square_sticker ( image , frame_gray ):
    
   
    faces = face_detector.detectMultiScale(frame_gray , 1.3 )
    
    for face in faces :
        x, y , w , h = face
        
        sticker = cv2.resize ( sticker_lion , [w , h])
       
        for i in range (w) :
            for j in range (h) :
                
                if sticker [ i] [j] [0] == 0 and sticker [ i] [j] [1] == 0 and sticker [ i] [j] [2] == 0 :
                    sticker [i ][j ] = image [y +i , x+ j] 

        image [y : y + h ,  x : x + w   ] = sticker

    return image

def lips_eyes_stickers (image , frame_gray):
    eyes = eye_detector.detectMultiScale ( frame_gray, 1.5 , maxSize= (50, 50))
    lips = lips_detector.detectMultiScale (frame_gray, 1.3 , 50 )

    if image.shape [2] == 4 :
        image = image [: , : , :3]



    for lip in lips:
        x , y , w , h = lip
        sticker_lips_resized = cv2.resize (sticker_lips , (w,h))
        
        # for i in range (w) :
        #     for j in range (h) :
                
        #         if sticker_lips_resized [ i] [j] [0] == 0 and sticker_lips_resized [ i] [j] [1] == 0 and sticker_lips_resized [ i] [j] [2] == 0 :
        #             sticker_lips_resized [i ][j ] = image [y +i , x+ j] 

        # image [y : y + h ,  x : x + w   ] = sticker_lips_resized
        

        sticker_alpha_lips = sticker_lips_resized[:, : , 2] / 255
        sticker_inv_alpha_lips = 1.0 - sticker_alpha_lips
        face_region_lips = image[y : y + h, x : x  + w]

        for channel in range(3):
            face_region_lips[:, :, channel] = (sticker_alpha_lips * sticker_lips_resized[:, :, channel] +
                                        sticker_inv_alpha_lips * face_region_lips[:, :, channel])

    if len(eyes) >= 2:
        x_mid = sum((x + w // 2) for (x, y, w, h) in eyes) / len(eyes)
        y_mid = sum((y + h // 2) for (x, y, w, h) in eyes) / len(eyes)

        width, height = 150, 100

        x_sticker = x_mid - width // 2
        y_sticker = y_mid - height // 2

        glasses = cv2.resize(sticker_sunglasses, (width, height))

        glass_alpha = glasses[:, :, 2] / 255
        sticker_inv_alpha = 1 - glass_alpha
        face_region = image[int(y_sticker):int(
            y_sticker + height), int(x_sticker):int(x_sticker + width)]

        for channel in range(3):
            face_region[:, :, channel] = (glass_alpha * glasses[:, :, channel] +
                                    sticker_inv_alpha * face_region[:, :, channel])


    return image

def mirror (image ):
    col = image.shape [1]
    flip_vertical = cv2.flip ( image[: ,  col//2 : ] ,1 )
    image [: ,  :col//2 ] = flip_vertical
    

    return image

def chess_board (image , frame_gray ):
    
    faces = face_detector.detectMultiScale( frame_gray , 1.3 , 5 )

    for face in faces :
        x , y , w , h = face
        face_image = image [ y : y + h , x : x + w]
        face_image_small = cv2.resize (face_image , [10,10])
        # cv2.imshow ("1" , face_image_small)

        face_image_big =cv2.resize (face_image_small ,[w,h],interpolation= cv2.INTER_NEAREST)
        # cv2.imshow ("2" , face_image_big)

        image [ y : y + h , x : x+w] = face_image_big
        # cv2.imshow ("chess" , image)

    
    return image
    



    

def show_menu () :
    print ("1- A non-square sticker on your face")
    print ("2- Stickers on your eyes and lips")
    print ("3- Chess-board face")
    print ("4- Mirror filter")
    print ("q- exit")
    


print ("Welcome to my face filter app")
print ( "Loading your video capture...")
show_menu ()
capture = cv2.VideoCapture (0)

face_detector = cv2.CascadeClassifier (cv2.data.haarcascades+"haarcascade_frontalface_default.xml")
eye_detector = cv2.CascadeClassifier (cv2.data.haarcascades+"haarcascade_eye.xml")
lips_detector = cv2.CascadeClassifier (cv2.data.haarcascades+"haarcascade_smile.xml")

sticker_lion = cv2.imread ("assignment3\HW4-3-3_facefilters\stickers\lion.png")
sticker_lips = cv2.imread ("assignment3\HW4-3-3_facefilters\stickers\lips.png")
sticker_sunglasses = cv2.imread ("assignment3\HW4-3-3_facefilters\stickers\sunglasses.png")


 
  





choice = 0

while True : 
    
    _ , frame = capture.read ()
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
       

    if choice == 1 :
        frame = non_square_sticker (frame , frame_gray)


    elif choice == 2 :
        frame = lips_eyes_stickers (frame , frame_gray)

    elif choice == 3 :
        
            
        frame = chess_board (frame , frame_gray) 
        # cv2.imshow ("result1" , frame)
           
             


    elif choice == 4 :
        frame = mirror (frame)

    cv2.imshow ("result" , frame)


      

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    elif cv2.waitKey(5) & 0xFF == ord('1'):
        choice = 1
    elif cv2.waitKey(5) & 0xFF == ord('2'):
        choice = 2
    elif cv2.waitKey(5) & 0xFF == ord('3'):
        choice = 3
    elif cv2.waitKey(5) & 0xFF == ord('4'):
        choice = 4
   
