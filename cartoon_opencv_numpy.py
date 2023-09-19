import cv2
import numpy as np
# Reading image
img = cv2.imread("./Images/photo2.webp")
# Show the output
# cv2.imshow('input', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
def cartoonize(img, k):
    # Defining input data for clustering
    data = np.float32(img).reshape((-1, 3))
    print("shape of input data: ", img.shape)
    print('shape of resized data', data.shape)
    # Defining criteria
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 20, 1.0)
    # Applying cv2.kmeans function
    _, label, center = cv2.kmeans(data, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
    center = np.uint8(center)
    print(center)
    # Reshape the output data to the size of input image
    result = center[label.flatten()]
    result = result.reshape(img.shape)
    # cv2.imshow("result", result)
    cv2.imwrite('./Images/Output/photo2_cartoon_2.jpg', result)
    # Convert the input image to gray scale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Perform adaptive threshold
    edges  = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 9, 8)
    cv2.imshow('Edge',edges)
    cv2.waitKey(0)
    blurred = cv2.medianBlur(result, 5)
    cv2.imshow('blurImage',blurred)
    cv2.waitKey(0)
    # Combine the result and edges to get final cartoon effect
    cartoon = cv2.bitwise_and(blurred, blurred, mask=edges)
    # cv2.imwrite('./Images/Output/photo2_cartoon_output.jpg', cartoon)
    cv2.imshow('cartoon',cartoon)
    cv2.waitKey(0)
cartoonize(img, 8)
