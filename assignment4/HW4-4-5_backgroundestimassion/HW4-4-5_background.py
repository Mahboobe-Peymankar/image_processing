import cv2
import numpy as np


video = cv2.VideoCapture("assignment4\HW4-4-5_backgroundestimassion\input\cars.mp4")

frame_count = video.get(cv2.CAP_PROP_FRAME_COUNT)

frames = []

for i in range(25):
    frame_id = np.random.randint(0, frame_count)
    video.set(cv2.CAP_PROP_POS_FRAMES, frame_id)
    _, frame = video.read()
    frames.append(frame)

median_frame = np.median(frames, axis=0).astype(np.uint8)
cv2.imwrite("assignment4\HW4-4-5_backgroundestimassion/result.png",median_frame)

cv2.imshow("frame", median_frame)
cv2.waitKey()