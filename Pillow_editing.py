from PIL import Image, ImageFilter, ImageOps, ImageEnhance
import cv2

img = Image.open('./Images/photo1.jpeg')
angle = 40
r_img = img.rotate(angle)
r_img.show()


def apply_cartoon_effect(input_image_path, cartoon_intensity=2):
    # Open the input image
    image = input_image_path
    smoothed_image = image.filter(ImageFilter.MedianFilter(size=7))
    edges = smoothed_image.filter(ImageFilter.FIND_EDGES)
    cartoon_image = Image.blend(smoothed_image, edges, alpha=cartoon_intensity)
    enhancer = ImageEnhance.Contrast(cartoon_image)
    cartoon_image = enhancer.enhance(3.5)
    cartoon_image = ImageOps.invert(cartoon_image)
    cartoon_image.show()

apply_cartoon_effect(img)