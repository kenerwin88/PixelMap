

import os

from PIL import Image

import imageDataTools



def get_image_int8rgb_pixels(filename):
    image = Image.open(filename)
    pixels = [item[:3] for item in image.getdata()]
    return pixels


def save_int8rgb_tuples_as_half_hex(data, output_filename=None, mode=None, decoration="{output_filename} = \"{result}\"", **other_kwargs):
    #does not save when output_filename is None.
    if output_filename is not None:
        if mode is None:
            raise ValueError("mode not specified")
    result = imageDataTools.int8rgb_pixels_to_hex(data, chars_per_channel=1, **other_kwargs)
    if output_filename is None:
        return result
    else:
        with open(output_filename, mode) as output_file:
            assert "{output_filename}" in decoration
            assert "{result}" in decoration
            decorated_result = decoration.replace("{output_filename}", output_filename).replace("{result}", result)
            output_file.write(decorated_result)
        return result


def print_all(folder_name, file_delimiter="\n---\n", file_decoration="{name}: {content}"):
    justStarted = True
    for scanFileName in os.listdir(folder_name):
        scanFullFileName = folder_name + "/" + scanFileName
        content = save_int8rgb_tuples_as_half_hex(get_image_int8rgb_pixels(scanFullFileName))
        printString = file_decoration.replace("{name}", scanFullFileName).replace("{content}", content)
        if justStarted:
            justStarted = False
        else:
            print(file_delimiter)
        print(printString)  

assert save_int8rgb_tuples_as_half_hex(get_image_int8rgb_pixels("images/1x1.png"), pixel_header="") =='390390390390390390390000000390390390390390390390390390390390390390000ff0ff0000390390390390390390390390390390390390000ff0ff0000390390390390390390390390390390390000ff0ff0ff0ff0000390390390390390000000000000000000ff0ff0ff0ff0000000000000000000000ff0ff0ff0ff0ff0ff0ff0ff0ff0ff0ff0ff0ff0ff0000390000ff0ff0ff0ff0000ff0ff0000ff0ff0ff0ff0000390390390000ff0ff0ff0000ff0ff0000ff0ff0ff0000390390390390390000ff0ff0000ff0ff0000ff0ff0000390390390390390390000ff0ff0ff0ff0ff0ff0ff0ff0000390390390390390000ff0ff0ff0ff0ff0ff0ff0ff0ff0ff0000390390390390000ff0ff0ff0ff0ff0ff0ff0ff0ff0ff0000390390390000ff0ff0ff0ff0ff0000000ff0ff0ff0ff0ff0000390390000ff0ff0ff0000000390390000000ff0ff0ff0000390000ff0ff0000000390390390390390390000000ff0ff0000000000000390390390390390390390390390390000000000'
