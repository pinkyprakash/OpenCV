import cv2
import numpy as np

img = cv2.imread('Sana.JPG',1)
img = cv2.resize(img,(500,600))


#Draw Line
img = cv2.line(img,(20,40),(150,40),(255,0,0),5)
#Draw Line Arraow
img = cv2.arrowedLine(img,(0,255),(200,255),(255,0,0),5)
#Draw Rectangle
img = cv2.rectangle(img,(100,40), (400,430),(0,255,0),5 )
#Draw Circle
img = cv2.circle(img,(250,250),200, (0,0,255),5)
#Draw Text in Image
font = cv2.FONT_HERSHEY_SIMPLEX
img = cv2.putText(img,'Sana',(150,500),font,3,(0,255,255),5,cv2.LINE_AA)
cv2.imshow('image',img)
key = cv2.waitKey(0) & 0xFF
if key == 27:
    cv2.destroyAllWindows()
