import cv2
from matplotlib import pyplot as plt
import numpy as np

img = cv2.imread('messi5.jpg',cv2.IMREAD_GRAYSCALE)
#img = cv2.imread('sudoku.png',cv2.IMREAD_GRAYSCALE)
#lap = cv2.Laplacian(img,cv2.CV_64F,ksize=3)
#Default kernal size is 1
lap = cv2.Laplacian(img,cv2.CV_64F,ksize=3)
#overide
lap = np.uint8(np.absolute(lap))

sobelX = cv2.Sobel(img,cv2.CV_64F,1,0)
sobelX = np.uint8(np.absolute(sobelX))

sobelY = cv2.Sobel(img,cv2.CV_64F,0,1)
sobelY = np.uint8(np.absolute(sobelY))

canyedges = cv2.Canny(img,100,200)

sobelCombained = cv2.bitwise_or(sobelX,sobelY)
titles = ['Original Image','Laplacian','sobelx','sobelY','sobelCombained','Canny']
images = [img,lap,sobelX,sobelY,sobelCombained,canyedges]

for i in range(6):
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()