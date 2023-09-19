import cv2
import numpy as np

# open an image using opencv
imgOriginal = cv2.imread("./Images/photo1.jpeg")
img = cv2.resize(imgOriginal, (400, 400))

# get image height and width
height, width, channels = img.shape

img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
cv2.imshow("img_gray",img_gray)
cv2.waitKey(0)
img_blur = cv2.GaussianBlur(img_gray, (21, 21), 0, 0)
cv2.imshow("img_blur",img_blur)
cv2.waitKey(0)
img_blend = cv2.divide(img_gray, img_blur, scale=256)
cv2.imshow("img_blend",img_blend)
cv2.waitKey(0)


grey= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
grey = cv2.medianBlur(grey, 5)
edges= cv2.adaptiveThreshold (grey, 255, cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY, 9, 2)
#cartoonize
color = cv2.bilateralFilter(img, 9, 250, 250)
cartoon = cv2.bitwise_and (color, color, mask = edges)
# cv2.imshow("edges", edges)
# cv2.waitKey(0)
# cv2.imshow("Image", img)
# cv2.waitKey(0)
cv2.imshow("Cartoon", cartoon)
cv2.waitKey(0)

sepia_filter = np.array([[0.393, 0.769, 0.189],
                            [0.349, 0.686, 0.168],
                            [0.272, 0.534, 0.131]])

sepia_image = cv2.transform(img, sepia_filter)
# result = cv2.addWeighted(sepia_image, 0.7, img_blur, 0.3, 0)
# cv2.imshow('result', result)
# cv2.waitKey(0)
cv2.imshow('sepia_image', sepia_image)
cv2.waitKey(0)

emboss_kernel = np.array([[-2, -1, 0],
                            [-1,  1, 1],
                            [ 0,  1, 2]])
embossed_image = cv2.filter2D(img, -1, emboss_kernel)
cv2.imshow('embossed_image', embossed_image)
cv2.waitKey(0)

infrared_image = cv2.applyColorMap(grey, cv2.COLORMAP_HOT)
cv2.imshow('infrared_image', infrared_image)
cv2.waitKey(0)

temp_image = cv2.resize(img, (50, 50), interpolation=cv2.INTER_LINEAR)
pixelated_image = cv2.resize(temp_image, (width, height), interpolation=cv2.INTER_NEAREST)
cv2.imshow('pixelated_image', pixelated_image)
cv2.waitKey(0)

negative_image = 250 - img
cv2.imshow('negative_image', negative_image)
cv2.waitKey(0)


# def watercolor_effect(img):
    
#     # Apply bilateral filter multiple times for a watercolor effect
#     for _ in range(5):
#         image = cv2.bilateralFilter(img, d=9, sigmaColor=9, sigmaSpace=7)
    
#     return image

# image = watercolor_effect(img)
# cv2.imshow('image', image)
# cv2.waitKey(0)
# save image using opencv
# cv2.imwrite('./Images/Output/photo1_PencilSketch.jpg', img_blend)