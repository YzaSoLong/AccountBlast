from PIL import Image

image = Image.open('screen_shot/rose.jpeg')

#image.show()

image_data = image.load()

height, width = image.size

for loop1 in range(height):
    for loop2 in range(width):
        r, g, b = image_data[loop1, loop2]
        image_data[loop1, loop2] = 0, 0, 0
image.save('screen_shot/roseT.jpeg')
