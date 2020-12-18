import cv2
from matplotlib import pyplot as plt

img = cv2.imread('gradient.png')
_,threshold_1 = cv2.threshold(img,50,255,cv2.THRESH_BINARY)
_,threshold_2 = cv2.threshold(img,50,255,cv2.THRESH_BINARY_INV)
_,threshold_3 = cv2.threshold(img,50,255,cv2.THRESH_TRUNC)
_,threshold_4 = cv2.threshold(img,50,255,cv2.THRESH_TOZERO)
_,threshold_5 = cv2.threshold(img,50,255,cv2.THRESH_TOZERO_INV)

title = ['Original Image','THRESH_BINARY','THRESH_BINARY_INV','THRESH_TRUNC','THRESH_TOZERO','THRESH_TOZERO_INV']
images = [img,threshold_1,threshold_2,threshold_3,threshold_4,threshold_5]

for i in range(6):
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
    plt.title(title[i])
    plt.xticks([]),plt.yticks([])

plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
