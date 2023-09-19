import cv2
import numpy as np
from skimage import io, color, img_as_ubyte, util
from skimage.restoration import denoise_bilateral
from skimage.color import rgb2hsv, hsv2rgb

# open an image using opencv
imgOriginal = cv2.imread("./Images/photo1.jpeg")
cv2.imshow("imgOriginal",imgOriginal)
cv2.waitKey(0)
img = cv2.resize(imgOriginal, (400, 400))
img2 = cv2.resize(imgOriginal, (400, 400))

# get image height and width
height, width, channels = img.shape

# gray image
img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
# cv2.imwrite('./Images/Output/photo_gray.jpg', img_gray)
cv2.imshow("img_gray",img_gray)
cv2.waitKey(0)

# blur image
img_blur = cv2.GaussianBlur(img_gray, (21, 21), 0, 0)
# cv2.imwrite('./Images/Output/photo_blur.jpg', img_blur)
cv2.imshow("img_blur",img_blur)
cv2.waitKey(0)

# convert into sktch
img_blend = cv2.divide(img_gray, img_blur, scale=256)
# cv2.imwrite('./Images/Output/photo_blend.jpg', img_blend)
cv2.imshow("img_blend",img_blend)
cv2.waitKey(0)


# convert border into white and remaining part of image is black
edges_image = cv2.Canny(img, 100, 200)
# cv2.imwrite('./Images/Output/photo_edge.jpg', edges_image)
cv2.imshow("edges_image", edges_image)
cv2.waitKey(0)

# edge image
grey= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
grey = cv2.medianBlur(grey, 5)
edges= cv2.adaptiveThreshold (grey, 255, cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY, 9, 2)
# cv2.imwrite('./Images/Output/photo_edges.jpg', edges)
cv2.imshow("edges", edges)
cv2.waitKey(0)

# color_edge image
colors = cv2.bilateralFilter(img, 9, 250, 250)
color_edge = cv2.bitwise_and (colors, colors, mask = edges)
# cv2.imwrite('./Images/Output/photo_color_edge.jpg', color_edge)
cv2.imshow('color_edge', color_edge)
cv2.waitKey(0)

# shepia image
sepia_filter = np.array([[0.393, 0.769, 0.189],
                             [0.349, 0.686, 0.168],
                             [0.272, 0.534, 0.131]])

sepia_image = cv2.transform(img, sepia_filter)
# cv2.imwrite('./Images/Output/photo_sepia.jpg', sepia_image)
cv2.imshow('sepia_image', sepia_image)
cv2.waitKey(0)

# embossed_image
emboss_kernel = np.array([[-2, -1, 0],
                            [-1,  1, 1],
                            [ 0,  1, 2]])
embossed_image = cv2.filter2D(img, -1, emboss_kernel)
# cv2.imwrite('./Images/Output/photo_embossed.jpg', embossed_image)
cv2.imshow('embossed_image', embossed_image)
cv2.waitKey(0)

# infrared_image
infrared_image = cv2.applyColorMap(grey, cv2.COLORMAP_HOT)
# cv2.imwrite('./Images/Output/photo_infrared.jpg', infrared_image)
cv2.imshow('infrared_image', infrared_image)
cv2.waitKey(0)

# pixelated_image
temp_image = cv2.resize(img, (50, 50), interpolation=cv2.INTER_LINEAR)
pixelated_image = cv2.resize(temp_image, (width, height), interpolation=cv2.INTER_NEAREST)
# cv2.imwrite('./Images/Output/photo_pixelated.jpg', pixelated_image)
cv2.imshow('pixelated_image', pixelated_image)
cv2.waitKey(0)

#tilt_shift_effect
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
tilt_shift_effect(img)

def cartoonize_skimage(image_path):
    image = image_path
    gray_image = color.rgb2gray(image)
    smoothed_image = denoise_bilateral(gray_image, sigma_color=0.05, sigma_spatial=15)
    num_bins = 8
    quantized_image = np.floor(smoothed_image * num_bins) / num_bins
    cartoon_image = np.stack([quantized_image] * 3, axis=-1)
    cartoon_image = img_as_ubyte(cartoon_image)
    cv2.imshow("cartoon_image",cartoon_image)
    cv2.waitKey(0)
    # return cartoon_image

cartoonize_skimage(img)

def vignette_effect(image_path, strength=0.5):
    # Load the image
    image = image_path
    gray_image = color.rgb2gray(image)
    rows, cols = gray_image.shape
    x, y = np.meshgrid(np.arange(cols), np.arange(rows))
    center_x, center_y = cols / 2, rows / 2
    distance = np.sqrt((x - center_x) ** 2 + (y - center_y) ** 2)
    max_distance = np.sqrt(center_x ** 2 + center_y ** 2)
    vignette_mask = 1 - (distance / max_distance)
    vignette_result = gray_image * vignette_mask * strength
    vignette_result = img_as_ubyte(vignette_result)
    cv2.imshow("vignette_result",vignette_result)
    cv2.waitKey(0)
    # return vignette_result
vignette_effect(img2)

def warhol_effect(image_path):
    # Load the image
    image = image_path

    # Convert the image to HSV color space
    hsv_image = rgb2hsv(image)

    # Modify the hue channel to create a Warhol-like effect
    num_repeats = 4
    hsv_image[:, :, 0] = np.tile(np.linspace(0, 1, num_repeats), (image.shape[0], image.shape[1] // num_repeats))

    # Convert back to RGB color space
    warholized_image = hsv2rgb(hsv_image)

    # Convert to 8-bit format for display
    warholized_image = img_as_ubyte(warholized_image)
    cv2.imshow("warholized_image",warholized_image)
    cv2.waitKey(0)

    # return warholized_image
warhol_effect(img)