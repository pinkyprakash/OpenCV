import cv2

img1 = cv2.imread('Sana.JPG')
img2 = cv2.imread('Sujan.JPG')
img1 = cv2.resize(img1,(512,512))
img2 = cv2.resize(img2,(512,512))


#dst = cv2.add(img1, img2)

dst = cv2.addWeighted(img1, .9, img2, .1,0)

cv2.imshow('image',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()