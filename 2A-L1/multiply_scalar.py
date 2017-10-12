import cv2
import numpy as np

# Multiply by scalar

img = cv2.imread("images/dolphin.png")
cv2.imshow("Dolphin image", img)

print "Dolphin image shape is \n {}".format(img.shape)

reduced_intensity = 0.5 * img
increased_intensity = 1.5 * img

cv2.imshow("Reduced intensity", reduced_intensity.astype(np.uint8))
cv2.imshow("Increased intensity", increased_intensity.astype(np.uint8))

cv2.waitKey(0)