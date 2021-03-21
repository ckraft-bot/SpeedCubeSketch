import cv2

#read
img = cv2.imread("Rubik.jpg")
#convert to grey
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#invert
invert_img = cv2.bitwise_not(gray_img)
#blur
blur_img = cv2.GaussianBlur(invert_img, (21,21),0)
#invert blur
invert_blur_img = cv2.bitwise_not(blur_img)
sketch = cv2.divide(gray_img, invert_blur_img, scale=256.0)



##TADA!!##
cv2.imwrite("Rubik.png", sketch)