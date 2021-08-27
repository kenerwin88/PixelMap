

from PIL import Image





def get_image_int8rgb_pixels(filename):
    image = Image.open(filename)
    pixels = [item[:3] for item in image.getdata()]
    return pixels
    
def save_as_hex_triplets(output_filename, data):
    pass