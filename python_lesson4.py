from PIL import Image

image = Image.open("monro.jpg")
red, blue, green = image.split()

coordinates_1 = (100, 0, red.width, red.height)
coordinates_2 = (50, 0,red.width - 50, red.height)
red_left = red.crop(coordinates_1)
red_middle = red.crop(coordinates_2)
new_red = Image.blend(red_left, red_middle, 0.5)

coordinates_1 = (0, 0, blue.width - 100, blue.height)
coordinates_2 = (50, 0,blue.width - 50, blue.height)
blue_right = blue.crop(coordinates_1)
blue_middle = blue.crop(coordinates_2)
new_blue = Image.blend(blue_right, blue_middle, 0.5)

coordinates = (50, 0, green.width - 50, green.height)
new_green = green.crop(coordinates)

new_image = Image.merge("RGB", (new_red, new_blue, new_green))
new_image.save("new_monro.jpg")

new_image.thumbnail((80,80))
new_image.save("avatar.jpg")