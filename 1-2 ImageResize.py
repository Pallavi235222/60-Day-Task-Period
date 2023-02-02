
from PIL import Image
import os

def resize_images(folder, new_width, new_height):
    for filename in os.listdir(folder):
        img = Image.open(f'{folder}/{filename}')
        img = img.resize((new_width, new_height), Image.ANTIALIAS)
        img.save(f'{folder}_resized/{filename}')

folder = input("Enter the name of the folder containing the images: ")
new_width = int(input("Enter the desired width for the images: "))
new_height = int(input("Enter the desired height for the images: "))

try:
    os.mkdir(f'{folder}_resized')
except FileExistsError:
    pass

resize_images(folder, new_width, new_height)
print("Images resized successfully!")


