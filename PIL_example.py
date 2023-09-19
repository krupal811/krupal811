from PIL import Image

image = Image.open('./Images/photo1.jpeg')

image.show('person1.jpg')

for x in range(image.size[0]):
    for y in range(image.size[1]):
        if image.getpixel((x,y))[0] > 200:
            image.putpixel((x,y),(0,0,255))
image.show('person2.jpg')