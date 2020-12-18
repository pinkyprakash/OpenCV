import cv2

img = cv2.imread('lena.jpg')
layer = img.copy()
gp = [layer]

for index in range(6):
    layer = cv2.pyrDown(layer)
    gp.append(layer)
    #cv2.imshow(str(index),layer)

layer = gp[5]
cv2.imshow('Upper level of Gaussian pyramid', layer)
lp = [layer]

for index in range(5,0,-1):
    gaussian_extended = cv2.pyrUp(gp[index])
    laplacian = cv2.subtract(gp[index-1],gaussian_extended)
    cv2.imshow(str(index),laplacian)

cv2.waitKey(0)
cv2.destroyAllWindows()