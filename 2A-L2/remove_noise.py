# Remove noise with a Gaussian filter

import cv2
import numpy as np 

# Load image
saturn = cv2.imread("images/saturn.png", 0)
cv2.imshow("Saturn without noise", saturn)

# Generate noise
noise_sigma = 25;
r , c = saturn.shape
noise = np.random.randn(r, c) * noise_sigma
noisy_saturn = saturn + noise

# Show noisy image
cv2.imshow("Saturn with noise", noisy_saturn.astype(np.uint8))

# Create Gaussian filter
filter_size = 11
filter_sigma = 2
filter_kernel = cv2.getGaussianKernel(filter_size,filter_sigma)

# Generate 2D kernel
filter_kernel = filter_kernel * filter_kernel.T

# Apply filter to noisy image
smooth_saturn = cv2.filter2D(noisy_saturn, -1, filter_kernel)
cv2.imshow("Smooth saturn", smooth_saturn.astype(np.uint8))

cv2.waitKey(0)

