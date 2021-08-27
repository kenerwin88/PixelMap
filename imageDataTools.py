"""

python2 or python3.

"""

import itertools
from collections import deque



ALPHABET = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
#case is ignored by builtin int(), but int() can't go above base 36 anyway, so it probably doesn't matter.

def assert_equals(thing0, thing1):
    assert thing0 == thing1, "{} does not equal {}.".format(thing0, thing1)



def gen_chunks(input_seq, length):
    labeling_function = (lambda toLabel: toLabel[0]//length)
    labled_group_gen = itertools.groupby(enumerate(input_seq), labeling_function)
    unlabled_group_gen = (labeledGroup[1] for labeledGroup in labled_group_gen)
    #remove enumeration:
    result = ((itemB[1] for itemB in unlabledGroup) for unlabledGroup in unlabled_group_gen)
    return result



def int_to_base(value, base):
    if not value >= 0:
        raise ValueError("negative value: {}.".format(value))
    if not base >= 2:
        raise ValueError("invalid base: {}.".format(base))
    result = deque([])
    while value > 0:
        current_digit = value % base
        result.appendleft(current_digit)
        value //= base
    if len(result) == 0:
        result.appendleft(0)
    return list(result)
    
    
def int_seq_to_str(int_seq):
    return "".join(ALPHABET[item] for item in int_seq)


def int_to_base_str(value, base):
    return int_seq_to_str(int_to_base(value, base))
    
    
    
def int8rgb_color_is_valid(color):
    return len(color) == 3 and min(color) >= 0 and max(color) < 256
    
    
def int8rgb_color_component_to_hex(component, length=2):
    assert 0 < length <= 2
    assert 0 <= component < 256
    result = int_to_base_str(component, 16)
    result = result.rjust(2, ALPHABET[0])
    assert len(result) == 2
    result = result[:length]
    return result


def int8rgb_color_to_hex(color, length=2, component_header="", component_delimiter=""):
    assert 0 < length <= 2
    assert int8rgb_color_is_valid(color)
    return component_delimiter.join(component_header + int8rgb_color_component_to_hex(value, length=length) for value in color)
    

def int8rgb_pixels_to_hex(pixels, chars_per_channel=2, pixel_header="", pixel_delimiter="", component_header="", component_delimiter=""):
    pixel_generator = (pixel_header + int8rgb_color_to_hex(color, length=chars_per_channel, component_header=component_header, component_delimiter=component_delimiter) for color in pixels)
    return pixel_delimiter.join(pixel_generator)
    

def int8rgb_pixel_rows_to_hex(pixels, auto_row_length=None, row_header="", row_delimiter="", **other_kwargs):
    if auto_row_length is not None:
        input_row_generator = gen_chunks(pixels, length=auto_row_length)
    else:
        input_row_generator = pixels
    output_row_generator = (row_header + int8rgb_pixels_to_hex(pixel_row, **other_kwargs) for pixel_row in input_row_generator)
    return row_delimiter.join(output_row_generator)



def gen_triplet_tuples_from_int_seq(int_seq):
    current_triplet = []
    for i, item in enumerate(int_seq):
        current_triplet.append(item)
        if len(current_triplet) == 3:
            yield tuple(current_triplet)
            current_triplet = []
    if not len(current_triplet) == 0:
        raise ValueError("int seq had invalid length {} (not divisible by 3).".format(i))
        
        
def int_lists_to_triplet_tuple_lists(int_list_seq):
    raise NotImplementedError()





    
def test():
    assert_equals(int8rgb_color_to_hex([255,255,255], component_delimiter="!"), "ff!ff!ff")

    for test_int in [0,1,2,3,5,8,13,21,34,55,127,128,129,255]:
        assert_equals(int(int8rgb_color_component_to_hex(test_int), 16), test_int)
        
    assert_equals(int8rgb_color_to_hex([14,15,16], length=2, component_header="?", component_delimiter="!"), "?0e!?0f!?10")
    assert_equals(int8rgb_color_to_hex([14,15,16], length=1, component_header="?", component_delimiter="!"), "?0!?0!?1")

    assert_equals(int8rgb_pixels_to_hex([[14,15,16], [30,31,32]], chars_per_channel=2, pixel_header="#", component_delimiter=","), "#0e,0f,10#1e,1f,20")
    
    assert_equals(int8rgb_pixel_rows_to_hex([[14,15,16], [30,31,32]], auto_row_length=2), int8rgb_pixels_to_hex([[14,15,16], [30,31,32]]))


test()


