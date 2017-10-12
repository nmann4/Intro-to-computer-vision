# Color planes

import cv2

img = cv2.imread("images/fruit.png")
cv2.imshow("Original Fruit Image", img)

print img.shape

# TODO: Select a color plane, display it, inspect values from a row

# Red, Green, and blue color planes
# OpenCV uses BGR
red = img[:, :, 2]
green = img[:, : , 1]
blue = img[:, :, 0]

cv2.imshow("Red color plane", red)
cv2.imshow("Green color plane", green)
cv2.imshow("Blue color plane", blue)

# Let's select the green plane, pick a row, and print the values
print "Green color plane, 100-th row \n {}".format(green[99, :])

# Let's draw a horizontal line across that row we picked
# But in order to see the line in color we need to convert green to a 3 - channel array
green_bgr = cv2.cvtColor(green, cv2.COLOR_GRAY2BGR)

# cv2.line uses x-y coordinate instead of row-cols
cv2.line(green_bgr, (0,99), (green.shape[1], 99), (0, 0, 225))
cv2.imshow("50-th row drawn on the green color plane", green_bgr)

cv2.waitKey(0)