from PIL import Image as pil_image, ImageOps
import os

image = pil_image.open('people.jpg')

# image = image.rotate(45)
# image = ImageOps.grayscale(image)
# image.convert('L')

# width, height = image.size
# print(width, height)
# image = image.resize((int(width*.1), int(height*.1)))

area = (500,500,800,800)
image = image.crop(area)

# source = image.split()
# r=0
# g=1
# b=2
# mask = source[r].point(lambda i : i<100 and 255)
# out = source[g].point(lambda i: i*2)
# source[g].paste(out,None, mask)
# image = pil_image.merge(image.mode, source)

# image.size()

image.show()