from skimage import io, color, img_as_ubyte, util
import skimage.filters as filters
from skimage.color import rgb2hsv, hsv2rgb
from skimage.restoration import denoise_bilateral
import numpy as np
import cv2

# open an image using opencv
imgOriginal = cv2.imread("./Images/photo1.jpeg")
cv2.imshow("imgOriginal",imgOriginal)
cv2.waitKey(0)
img = cv2.resize(imgOriginal, (400, 400))
img2 = cv2.resize(imgOriginal, (400, 400))

# def cartoonize_skimage(image_path):
#     image = image_path
#     gray_image = color.rgb2gray(image)
#     smoothed_image = denoise_bilateral(gray_image, sigma_color=0.05, sigma_spatial=15)
#     num_bins = 8
#     quantized_image = np.floor(smoothed_image * num_bins) / num_bins
#     cartoon_image = np.stack([quantized_image] * 3, axis=-1)
#     cartoon_image = img_as_ubyte(cartoon_image)
#     cv2.imshow("cartoon_image",cartoon_image)
#     cv2.waitKey(0)
#     # return cartoon_image

# cartoonize_skimage(img)

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
vignette_effect(img)

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