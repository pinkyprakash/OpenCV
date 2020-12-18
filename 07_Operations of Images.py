import cv2

img = cv2.imread('lena.jpg')
img = cv2.resize(img,(512,512))

print(img.shape)
print(img.size)
print(img.dtype)

b,g,r = cv2.split(img)
img = cv2.merge((b,g,r))


img = cv2.rectangle(img,(180,186), (386,230),(0,255,0),5)
head = img[180:186, 386:230]
img[188:125, 386:170] = head

cv2.imshow('image',img)

cv2.waitKey(0)
cv2.destroyAllWindows()