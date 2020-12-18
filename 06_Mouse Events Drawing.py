import cv2
import numpy as np

#events = [i for i in dir(cv2)]
#print(events)

def click_event(event,x,y,flag,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y),3,(0,0,255),-1)
        points.append((x,y))
        #Mouse clicked more than 2 timies or double clicked
        if len(points) >= 2:
            #last and 2nd last element in the array
            cv2.line(img,points[-1],points[-2], (255,0,0),5)
        cv2.imshow('image',img)
    if event == cv2.EVENT_RBUTTONDOWN:
        blue = img[x,y,0]
        green = img[y,x,1]
        red = img[y,x,2]
        cv2.circle(img, (x, y), 3, (0, 0, 255), -1)
        mycolorImg = np.zeros((512,512,3),np.uint8)
        mycolorImg[:] = [blue,green,red]
        cv2.imshow('color', mycolorImg)

img = cv2.imread('lena.JPG',1)
img = cv2.resize(img,(512,512))
#img = np.zeros((512,512,3), np.uint8)
cv2.imshow('image',img)
points  = []
cv2.setMouseCallback('image',click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()
