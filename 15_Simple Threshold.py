import cv2
import numpy as np

img = cv2.imread('gradient.png')
_,threshold_1 = cv2.threshold(img,50,255,cv2.THRESH_BINARY)
_,threshold_2 = cv2.threshold(img,50,255,cv2.THRESH_BINARY_INV)
_,threshold_3 = cv2.threshold(img,50,255,cv2.THRESH_TRUNC)
_,threshold_4 = cv2.threshold(img,50,255,cv2.THRESH_TOZERO)
_,threshold_5 = cv2.threshold(img,50,255,cv2.THRESH_TOZERO_INV)


cv2.imshow("image",img)
cv2.imshow("threshold_1",threshold_1)
cv2.imshow("threshold_2",threshold_2)
cv2.imshow("threshold_3",threshold_3)
cv2.imshow("threshold_4",threshold_4)
cv2.imshow("threshold_5",threshold_5)

cv2.waitKey(0)
cv2.destroyAllWindows()
