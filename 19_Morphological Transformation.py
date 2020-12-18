import cv2
from matplotlib import pyplot as plt
import numpy as np

img = cv2.imread('smarties.png',cv2.IMREAD_GRAYSCALE)
_,mask = cv2.threshold(img,220,255, cv2.THRESH_BINARY_INV)

kernal = np.ones((2,2),np.uint8)
dilation = cv2.dilate(mask,kernal,iterations=2)
erosion = cv2.erode(mask,kernal, iterations=2)
MORPH_ERODE = cv2.morphologyEx(mask, cv2.MORPH_ERODE,kernal)
MORPH_DILATE = cv2.morphologyEx(mask, cv2.MORPH_DILATE,kernal)
MORPH_OPEN = cv2.morphologyEx(mask, cv2.MORPH_OPEN,kernal)
MORPH_CLOSE = cv2.morphologyEx(mask, cv2.MORPH_CLOSE,kernal)
MORPH_BLACKHAT = cv2.morphologyEx(mask, cv2.MORPH_BLACKHAT ,kernal)
MORPH_CROSS = cv2.morphologyEx(mask, cv2.MORPH_CROSS ,kernal)
MORPH_ELLIPSE = cv2.morphologyEx(mask, cv2.MORPH_ELLIPSE ,kernal)
MORPH_BLACKHAT = cv2.morphologyEx(mask, cv2.MORPH_BLACKHAT ,kernal)
MORPH_GRADIENT = cv2.morphologyEx(mask, cv2.MORPH_GRADIENT ,kernal)
MORPH_HITMISS = cv2.morphologyEx(mask, cv2.MORPH_HITMISS ,kernal)
MORPH_RECT = cv2.morphologyEx(mask, cv2.MORPH_RECT  ,kernal)
MORPH_TOPHAT = cv2.morphologyEx(mask, cv2.MORPH_TOPHAT ,kernal)
MORPH_HITMISS = cv2.morphologyEx(mask, cv2.MORPH_HITMISS ,kernal)

titles = ['image','mask','dilation','erosion','MORPH_ERODE', 'MORPH_DILATE','MORPH_OPEN','MORPH_CLOSE','MORPH_BLACKHAT','MORPH_GRADIENT','MORPH_HITMISS','MORPH_RECT','MORPH_TOPHAT','MORPH_HITMISS']
images = [img,mask,dilation,erosion, MORPH_ERODE, MORPH_DILATE, MORPH_OPEN, MORPH_CLOSE,MORPH_BLACKHAT,MORPH_GRADIENT,MORPH_HITMISS,MORPH_RECT,MORPH_TOPHAT,MORPH_HITMISS]

for i in range(14):
    plt.subplot(4,4,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()