# image.py
from PIL import Image  # Ensure you import Pillow

class Pixel:
    def __init__(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue

class FileImage:
    def __init__(self, filename):
        self.image = Image.open(filename).convert('RGB')  # Convert to RGB
        self.pixels = self.image.load()

    def get_width(self):
        return self.image.width

    def get_height(self):
        return self.image.height

    def get_pixel(self, x, y):
        r, g, b = self.pixels[x, y]  # This will now work correctly if the image is in RGB mode
        return Pixel(r, g, b)

