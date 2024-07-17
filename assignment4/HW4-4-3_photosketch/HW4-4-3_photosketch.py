import cv2
import numpy as np

image = cv2.imread ("assignment4\HW4-4-3_photosketch\input/2.jpg")
image=cv2.cvtColor (image,cv2.COLOR_BGR2GRAY)

inverted_image = 255 - image
blured_image = cv2.GaussianBlur (inverted_image , (21,21), 0)
inverted_blured_image = 255 - blured_image

sketch = image/ inverted_blured_image
sketch = sketch * 255
sketh = sketch.astype(np.uint8)

cv2.imwrite ("assignment4\HW4-4-3_photosketch/result.jpg",sketch)
