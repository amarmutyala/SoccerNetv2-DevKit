import cv2 

# Window name in which image is displayed
window_name = 'Image'

image = cv2.imread('radar.png')


thickness = -1
  
# Using cv2.circle() method
# Draw a circle of red color of thickness -1 px
image = cv2.circle(image, (25,10), 10, (109, 133, 155), -1)
  
# Displaying the image
cv2.imshow(window_name, image)

cv2.waitKey(0)