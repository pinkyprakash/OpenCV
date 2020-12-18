import cv2
from matplotlib import pyplot as plt
import numpy as np

def nothing(x):
    pass

img = cv2.imread('messi5.jpg')

cv2.createTrackbar('t1','image',0,255,nothing)
cv2.createTrackbar('t2','image',0,255,nothing)

while True:
    Threshold1 = cv2.getTrackbarPos('t1', 'image')
    Threshold2 = cv2.getTrackbarPos('t2', 'image')
    canny = cv2.Canny(img, Threshold1, Threshold2)
    titles = ['Image', 'canny']
    images = [img, canny]
    for i in range(2):
        plt.subplot(1,2,i+1),plt.imshow(images[i],'gray')
        plt.title(titles[i])
        plt.xticks([]),plt.yticks([])
    plt.show()

    key = cv2.waitKey(1)
    if key == 27:
        break

cv2.destroyAllWindows()