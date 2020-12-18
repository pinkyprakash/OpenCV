import cv2
import numpy as np

img1 = np.zeros((250,500,3),np.uint8)
img1 = cv2.rectangle(img1,(200,0),(300,100),(255,255,255),-1)
img2 = cv2.imread("Sujan.JPG")
img2 = cv2.resize(img2,(500,250))

bitWiseAnd = cv2.bitwise_and(img2,img1)
bitWiseOr = cv2.bitwise_or(img2,img1)
bitWiseXOr = cv2.bitwise_xor(img2,img1)
bitWiseNot1 = cv2.bitwise_not(img1)
bitWiseNot2 = cv2.bitwise_not(img2)

cv2.imshow("img1",img1)
cv2.imshow("img2",img2)
#cv2.imshow("BitWiseAnd",bitWiseAnd)
#cv2.imshow("BitWiseOr",bitWiseOr)
#cv2.imshow("BitWiseXOr",bitWiseXOr)
#cv2.imshow("BitWiseNot",bitWiseNot1)
cv2.imshow("BitWiseNot",bitWiseNot2)

cv2.waitKey(0)
cv2.destroyAllWindows()