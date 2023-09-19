#import the packages
import cv2

# Load the image using cv2
img = cv2.imread("./Images/photo2.webp")
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

#Convert to grayscale and apply median blur to reduce image noise
grayimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
grayimg = cv2.medianBlur(grayimg, 5)
cv2.imshow('grayimg',grayimg)
cv2.waitKey(0)

#Get the edges 
edges = cv2.adaptiveThreshold(grayimg, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 5, 5)
cv2.imshow('edges',edges)
cv2.waitKey(0)

#Convert to a cartoon version
color = cv2.bilateralFilter(img, 9, 250, 250)
cv2.imshow('color',color)
cv2.waitKey(0)

cartoon = cv2.bitwise_and(color, color, mask=edges)
cv2.imshow('cartoon',cartoon)
cv2.waitKey(0)
# cv2.imwrite('./Images/Output/photo2_cartoon.jpg', cartoon)