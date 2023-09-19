#import the packages
import cv2

# Load the image using cv2
image = cv2.imread("./Images/photo3.jpeg")

image_resized = cv2.resize(image, None, fx=0.5, fy=0.5)

image_cleared = cv2.medianBlur(image_resized, 3)
image_cleared = cv2.medianBlur(image_cleared, 3)
image_cleared = cv2.medianBlur(image_cleared, 3)

image_cleared = cv2.edgePreservingFilter(image_cleared, sigma_s=5)
cv2.imshow("image_cleared", image_cleared)
cv2.waitKey(0)
image_filtered = cv2.bilateralFilter(image_cleared, 3, 10, 5)
cv2.imshow("image_filtered", image_filtered)
cv2.waitKey(0)
for i in range(2):
    image_filtered = cv2.bilateralFilter(image_filtered, 3, 20, 10)

for i in range(3):
    image_filtered = cv2.bilateralFilter(image_filtered, 5, 30, 10)

gaussian_mask= cv2.GaussianBlur(image_filtered, (7,7), 2)
cv2.imshow("gaussian_mask", gaussian_mask)
cv2.waitKey(0)
image_sharp = cv2.addWeighted(image_filtered, 1.5, gaussian_mask, -0.5, 0)
image_sharp = cv2.addWeighted(image_sharp, 1.4, gaussian_mask, -0.2, 10)
cv2.imshow("image_sharp", image_sharp)
cv2.waitKey(0)

# cv2.imwrite('./Images/Output/photo3_Art.jpg', image_sharp)