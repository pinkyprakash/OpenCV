#https://www.youtube.com/watch?v=N81PCpADwKQ&feature=youtu.be
import cv2

#print(cv2.__version__)
#print('This is first program from pyCharm')
#print(img.get(cv2.CAP_PROP_FRAME_WIDTH))
#print(img.get(cv2.CAP_PROP_FRAME_HEIGHT))

img = cv2.imread('Sujan.JPG',-1)
img = cv2.resize(img,(500,600))
cv2.imshow('image',img)

key = cv2.waitKey(0) & 0xFF

if key == 27:
    cv2.destroyAllWindows()
elif key == ord('s'):
    cv2.imwrite('Sujan_copy.jpg', img)
