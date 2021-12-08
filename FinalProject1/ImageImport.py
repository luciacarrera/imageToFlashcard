#import the vision library
import cv2
#load an image
image = cv2.imread("banana.png")
#display an image
cv2.imshow("Banana", image)
#wait with the image until any key is pressed
cv2.waitKey(0)
y = 0
x = 0
h = 30
w = 1100
crop_image = image[x:w, y:h]
cv2.imshow("Cropped", crop_image)
cv2.waitKey(0)
