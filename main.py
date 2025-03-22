from PIL import Image
import os
import json


def find_marker(img, colour):
    colour = tuple(colour)
    pixels = img.load()
    width, height = img.size

    for y in range(height):
        for x in range(width):
            print(pixels[x, y])
            if pixels[x, y][:3] == colour:
                return x, y


with open("config.json", 'r') as f:
    config = json.load(f)

img = Image.open("test.png")
marker = find_marker(img, config["parts"][0]["marker"])
print(marker)