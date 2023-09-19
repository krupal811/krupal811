import cv2
import numpy as np

# Load the image
image = cv2.imread('./Images/photo3.jpeg')
# Create a mask (black background)
mask = np.zeros(image.shape[:2], dtype=np.uint8)

# Initialize the background and foreground models for grabCut
bgdModel = np.zeros((1, 65), dtype=np.float64)
fgdModel = np.zeros((1, 65), dtype=np.float64)

# Define a rectangle around the object you want to keep (adjust the coordinates)
rect = (50, 50, image.shape[1] - 100, image.shape[0] - 100)

# Apply grabCut algorithm to segment the object
cv2.grabCut(image, mask, rect, bgdModel, fgdModel, 5, cv2.GC_INIT_WITH_RECT)

# Modify the mask to create a binary mask
mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')

# Multiply the original image with the binary mask to remove the background
result = image * mask2[:, :, np.newaxis]

# Display the result
cv2.imshow('Result', result)
cv2.waitKey(0)
cv2.destroyAllWindows()