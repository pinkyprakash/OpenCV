import cv2
import numpy as np

img = cv2.imread('sudoku.png',0)
_,threshold_1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
threshold_2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,11,2)
threshold_3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,11,2)

cv2.imshow("image",img)
cv2.imshow("threshold_1",threshold_1)
cv2.imshow("threshold_2",threshold_2)
cv2.imshow("threshold_3",threshold_3)

cv2.waitKey(0)
cv2.destroyAllWindows()