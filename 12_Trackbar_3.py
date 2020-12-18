import numpy as np
import cv2 as cv

def nothing(x):
    print(x)

#img = np.zeros((300,512,3),np.uint8)


cv.namedWindow('image')
cv.createTrackbar('CP','image',10,400,nothing)

switch = 'Color/Gray'
cv.createTrackbar(switch,'image',0,1,nothing)

while(1):
    img = cv.imread('lena.jpg')
    img = cv.resize(img, (500, 250))
    pos = cv.getTrackbarPos('CP', 'image')
    font = cv.FONT_HERSHEY_SIMPLEX
    cv.putText(img, str(pos), (50, 150), font, 6, (0, 255, 255),10)

    s = cv.getTrackbarPos(switch, 'image')

    if s == 0:
        pass
    else:
        img = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

    k =cv.waitKey(1) & 0xFF
    if k ==27:
        break
    img = cv.imshow('image',img)
cv.destroyAllWindows()