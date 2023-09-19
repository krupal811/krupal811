import cv2
import numpy as np
# open an image using opencv
imgOriginal = cv2.imread("./Images/photo1.jpeg")
cv2.imshow("imgOriginal",imgOriginal)
cv2.waitKey(0)
img = cv2.resize(imgOriginal, (400, 400))
img2 = cv2.resize(imgOriginal, (400, 400))
img3 = cv2.resize(imgOriginal, (400, 400))

def raindrops_effect(image_path):
    imggg = image_path
    # Generate random raindrop positions and intensities
    for _ in range(1000):
        x = np.random.randint(0, imggg.shape[1])
        y = np.random.randint(0, imggg.shape[0])
        cv2.circle(imggg, (x, y), 1, (175, 89, 225), -1)
    
    cv2.imshow("imggg",imggg)
    cv2.waitKey(0)
    # return imggg
raindrops_effect(img)

def raindrops_effect(image_path):
    image = image_path
    
    # Create a rotating kaleidoscope effect
    height, width, _ = image.shape
    num_slices = 12
    
    for i in range(num_slices):
        M = cv2.getRotationMatrix2D((width // 2, height // 2), i * (360 / num_slices), 1)
        image = cv2.warpAffine(image, M, (width, height))
    
    cv2.imshow("image",image)
    cv2.waitKey(0)
    # return image

raindrops_effect(img2)

def tilt_shift_effect(image_path):
    image = image_path
    
    # Apply Gaussian blur to the image
    blurred = cv2.GaussianBlur(image, (0, 0), sigmaX=10)
    
    # Create a mask for the transition between sharp and blurred regions
    mask = np.zeros_like(image)
    mask[200:400, :] = 1
    
    # Combine the sharp and blurred images using the mask
    result = image * mask + blurred * (1 - mask)
    cv2.imshow("result",result)
    cv2.waitKey(0)
    # return result
tilt_shift_effect(img3)