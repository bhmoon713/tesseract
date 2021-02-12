import numpy as np
import cv2


black = np.zeros((41,175), dtype=np.uint8)
cv2.imshow('black',black)
cv2.waitKey(0)