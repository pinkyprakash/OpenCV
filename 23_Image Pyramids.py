import cv2
import numpy as np

#Resolution loss
img = cv2.imread('lena.jpg')
lr1 = cv2.pyrDown(img)
lr2 = cv2.pyrDown(lr1)
lr3 = cv2.pyrDown(lr2)

hr2 = cv2.pyrUp(lr3)

cv2.imshow("Original image",img)
cv2.imshow("pyrDown 1",lr1)
cv2.imshow("pyrDown 2",lr2)
cv2.imshow("pyrDown 3",lr3)

cv2.imshow("pyrDown 3",hr2)

cv2.waitKey(0)
cv2.destroyAllWindows()