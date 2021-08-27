
from PIL import Image

import imageDataTools



def get_image_int8rgb_pixels(filename):
    image = Image.open(filename)
    pixels = [item[:3] for item in image.getdata()]
    return pixels


def save_int8rgb_tuples_as_half_hex(data, output_filename=None, mode=None, decoration="{output_filename} = \"{result}\"", **other_kwargs):
    if output_filename is not None:
        if mode is None:
            raise ValueError("mode not specified")
    result = imageDataTools.int8rgb_pixels_to_hex(chars_per_channel=1, **other_kwargs)
    if output_filename is None:
        return result
    else:
        with open(output_filename, mode) as output_file:
            assert "{output_filename}" in decoration
            assert "{result}" in decoration
            decorated_result = decoration.replace("{output_filename}", output_filename).replace("{result}", result)
            output_file.write(decorated_result)
        return result





