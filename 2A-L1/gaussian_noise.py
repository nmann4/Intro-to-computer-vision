# Apply gaussian noise to an image

import cv2
import numpy as np 

# Open image
saturn = cv2.imread("images/saturn.png")
cv2.imshow("Saturn without noise", saturn)

# Generate noise array equal to image size
noise = np.random.randn(480,640,3)
noisy_saturn = noise * saturn
cv2.imshow("Saturn with noise", noisy_saturn)

cv2.waitKey(0)

