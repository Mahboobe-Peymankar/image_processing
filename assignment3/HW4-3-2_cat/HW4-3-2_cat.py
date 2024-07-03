import cv2



image =  cv2.imread ("assignment3/HW4-3-2_cat/cat.png")

image_gray = cv2.cvtColor(image , cv2.COLOR_BGR2GRAY)


cat_detector = cv2.CascadeClassifier (cv2.data.haarcascades+"haarcascade_frontalcatface.xml")

cats=cat_detector.detectMultiScale(image_gray)
print (cats)
no_cat = 0
for cat in cats :
    x, y , w , h = cat
    cv2.rectangle (image , (x,y) , (x+w , y+h) ,(0,0,0) , 4)
    no_cat += 1

print ("there are ", no_cat , "cats in this picture")
cv2.imshow ("color", image)
cv2.imwrite  ("assignment3/HW4-3-2_cat/detectedcat.png" , image)

cv2.waitKey ()