import cv2

img= cv2.imread("target.jpg")
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imwrite("gray.jpg",gray_img)
inv_img = 255 - gray_img
cv2.imwrite("inverted.jpg", inv_img)
blurred = cv2.GaussianBlur(inv_img,(21,21), 0)
cv2.imwrite("blurred.jpg", blurred)
inv_blurred = 255 - blurred
cv2.imwrite("invertedblur.jpg", inv_blurred)
sketch = cv2.divide(gray_img,inv_img,scale=256.0)
cv2.imwrite("sketch.jpg", sketch)