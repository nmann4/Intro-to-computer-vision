# Add two images

import cv2

# Open bicycle and dolphin images
dolphin = cv2.imread("images/dolphin.png")
bicycle = cv2.imread("images/bicycle.png")

cv2.imshow("Dolphin image", dolphin)
cv2.imshow("Bicycle image", bicycle)

print "Dolphin image shape is \n {}".format(dolphin.shape)
print "Bicycle image shape is \n {}".format(bicycle.shape)

# Add the images in different ways
summed = dolphin + bicycle
average = dolphin / 2 + bicycle / 2
average_alt = (dolphin + bicycle) / 2

cv2.imshow("Summed image", summed)
cv2.imshow("Average image", average)
cv2.imshow("Alternate average image", average_alt)

cv2.waitKey(0)