import cv2

path=input("Path of image: ")
image = cv2.imread(path)
cv2.namedWindow("out", cv2.WINDOW_NORMAL)
  
gray_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
inverted_image = cv2.bitwise_not(gray_image)
blurred = cv2.GaussianBlur(inverted_image, (101, 101),0)
inverted_blurred = 255 - blurred
pencil_sketch = cv2.divide(gray_image, inverted_blurred, scale=256.0)
cv2.imshow("out", pencil_sketch)
cv2.waitKey(0)