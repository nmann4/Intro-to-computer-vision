# Blending two images

import cv2
import numpy as np 

# Blends 2 images together using a weight factor
def blend(a, b, alpha):
	"""
		Blends two images together using a weight factor
	"""
	return alpha * a + (1. - alpha) * b


# Open images
dolphin = cv2.imread("images/dolphin.png")
bicycle = cv2.imread("images/bicycle.png")

cv2.imshow("Dolphin", dolphin)
cv2.imshow("Bicycle", bicycle)

result = blend(dolphin,bicycle, 0.75)
cv2.imshow("Result", result.astype(np.uint8))

cv2.waitKey(0)