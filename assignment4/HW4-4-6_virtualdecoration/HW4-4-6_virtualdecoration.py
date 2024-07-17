import cv2
# import numpy as np

room_background = cv2.imread("assignment4\HW4-4-6_virtualdecoration\input/room.png")
room_foreground = cv2.imread("assignment4\HW4-4-6_virtualdecoration\input/floor_covering_image.png")
room_mask = cv2.imread("assignment4\HW4-4-6_virtualdecoration\input/room_mask.png")

normalized_mask = room_mask / 255.0

result_room_foreground = room_foreground * normalized_mask

mask_inverted = 255 - room_mask

normalized_mask_inverted = mask_inverted / 255.0

result_room_background = room_background * normalized_mask_inverted

result = result_room_foreground + result_room_background

cv2.imwrite("assignment4\HW4-4-6_virtualdecoration/result.png", result)