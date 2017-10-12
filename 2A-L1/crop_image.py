# Cropping an image

import cv2

# Open original image
img = cv2.imread("images/bicycle.png")
cv2.imshow("Bicycle image", img)

print img.shape

# Crop image
cropped = img[110:310, 10:160]
cv2.imshow("Cropped image", cropped)

print cropped.shape

cv2.waitKey(0)