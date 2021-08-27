

import os
import fnmatch

from PIL import Image

import imageDataTools



def get_image_int8rgb_pixels(filename):
    image = Image.open(filename)
    pixels = [item[:3] for item in image.getdata()]
    return pixels


def save_int8rgb_tuples_as_half_hex(data, output_filename=None, mode=None, decoration="{output_filename} = \"{result}\"", **other_kwargs):
    #does not save when output_filename is None.
    if decoration is None:
        decoration = "{result}"
    if output_filename is not None:
        if mode is None:
            raise ValueError("mode not specified")
    result = imageDataTools.int8rgb_pixels_to_hex(data, chars_per_channel=1, **other_kwargs)
    if output_filename is None:
        return result
    else:
        with open(output_filename, mode) as output_file:
            #assert "{output_filename}" in decoration
            assert "{result}" in decoration
            decorated_result = decoration.replace("{output_filename}", output_filename).replace("{result}", result)
            output_file.write(decorated_result)
        return result


def process_png_files(
        folder_name,
        file_name_pattern="*.png",
        create_files=False,
        output_filename_prefix="outputs/", output_filename_suffix=".txt",
        line_length=48,
        file_delimiter="\n---\n", file_decoration="{name}:\n{content}"):
        
    justStarted = True
    for scanFileName in os.listdir(folder_name):
        if not fnmatch.fnmatch(scanFileName, file_name_pattern):
            continue
        scanFullFileName = folder_name + "/" + scanFileName
        outputFileName = None
        if create_files:
            outputFileName = output_filename_prefix + scanFullFileName + output_filename_suffix
        content = save_int8rgb_tuples_as_half_hex(get_image_int8rgb_pixels(scanFullFileName), output_filename=outputFileName, mode="w", decoration=None)
        printString = file_decoration.replace("{name}", scanFullFileName).replace("{content}", content)
        if justStarted:
            justStarted = False
        else:
            print(file_delimiter)
        if line_length is not None:
            print_wrapped(printString, line_length=line_length)
        else:
            print(printString)




def print_wrapped(text, line_length=80):
    for line in text.split("\n"):
        i = 0
        while i < len(line):
            print(line[i:i+line_length])
            i += line_length





assert save_int8rgb_tuples_as_half_hex(get_image_int8rgb_pixels("images/1x1.png"), pixel_header="") =="\
    390390390390390390390000000390390390390390390390\
    390390390390390390000ff0ff0000390390390390390390\
    390390390390390390000ff0ff0000390390390390390390\
    390390390390390000ff0ff0ff0ff0000390390390390390\
    000000000000000000ff0ff0ff0ff0000000000000000000\
    000ff0ff0ff0ff0ff0ff0ff0ff0ff0ff0ff0ff0ff0ff0000\
    390000ff0ff0ff0ff0000ff0ff0000ff0ff0ff0ff0000390\
    390390000ff0ff0ff0000ff0ff0000ff0ff0ff0000390390\
    390390390000ff0ff0000ff0ff0000ff0ff0000390390390\
    390390390000ff0ff0ff0ff0ff0ff0ff0ff0000390390390\
    390390000ff0ff0ff0ff0ff0ff0ff0ff0ff0ff0000390390\
    390390000ff0ff0ff0ff0ff0ff0ff0ff0ff0ff0000390390\
    390000ff0ff0ff0ff0ff0000000ff0ff0ff0ff0ff0000390\
    390000ff0ff0ff0000000390390000000ff0ff0ff0000390\
    000ff0ff0000000390390390390390390000000ff0ff0000\
    000000000390390390390390390390390390390000000000"
