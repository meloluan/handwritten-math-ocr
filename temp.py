import cv2
import numpy as np

img = cv2.imread('3.jpeg',0)
ret,thresh = cv2.threshold(img,100,255,0)

img,contours,hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

cnt = contours[0]

x,y,w,h = cv2.boundingRect(cnt)
img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

cv2.imshow('img',img)

cv2.waitKey(0)
cv2.destroyAllWindows()
