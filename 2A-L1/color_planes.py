# Color planes

import cv2

img = cv2.imread("images/fruit.png")
cv2.imshow("Original Fruit Image", img)

print img.shape

# TODO: Select a color plane, display it, inspect values from a row

cv2.waitKey(0)