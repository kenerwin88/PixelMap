import json
from web3 import Web3, KeepAliveRPCProvider, IPCProvider
from PIL import Image

web3 = Web3(KeepAliveRPCProvider(host='localhost', port='8546'))
print(web3.isConnected())
abi = json.loads('[{"constant":true,"inputs":[{"name":"","type":"uint256"}],"name":"owners","outputs":[{"name":"","type":"address"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"x","type":"uint256"},{"name":"y","type":"uint256"}],"name":"buyTile","outputs":[],"payable":true,"type":"function"},{"constant":false,"inputs":[{"name":"x","type":"uint256"},{"name":"y","type":"uint256"}],"name":"getPos","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"","type":"uint256"}],"name":"urls","outputs":[{"name":"","type":"string"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"x","type":"uint256"},{"name":"y","type":"uint256"}],"name":"getTile","outputs":[{"name":"","type":"address"},{"name":"","type":"string"},{"name":"","type":"string"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"","type":"uint256"}],"name":"images","outputs":[{"name":"","type":"string"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"","type":"uint256"}],"name":"prices","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"x","type":"uint256"},{"name":"y","type":"uint256"},{"name":"image","type":"string"},{"name":"url","type":"string"},{"name":"price","type":"uint256"}],"name":"setPixel","outputs":[],"payable":false,"type":"function"},{"inputs":[],"type":"constructor"}]')

contract = web3.eth.contract(
    abi, address="0x1468804F7dC7020823defd910C5709C7B93fe295")


def chunk_str(str, chunk_size):
    return [str[i:i + chunk_size] for i in range(0, len(str), chunk_size)]


def get_position(x, y):
    return y * 16 + x


def double_mult(s):
    return ''.join([x * 2 for x in s])


class Pixel:

    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b


def hex_to_rgb(value):
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))


for x in range(81):    # for every pixel:
    for y in range(49):
        tile = contract.call().getTile(x, y)

        image_data = tile[2]
        if not image_data:
            image_data = '000000000000000000000000000000000000000000000000000777AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABBBAAA000000AAAFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFDDD000000AAAFFFFFFEEEEEEEEEEEEEEEEEEEEEEEEEEEFFFDDD000000AAAFFFEEEEEEFFFFFFEEEEEEFFFFFFEEEEEEFFFDDD000000AAAFFFEEEFFFAAA999DDDEEEAAAAAAEEEEEEFFFDDD000000AAAFFFEEEFFF999777BBBBBB888888EEEEEEFFFDDD000000AAAFFFEEEEEEDDDBBB888888AAADDDEEEEEEFFFDDD000000AAAFFFEEEEEEEEEBBB888777AAAEEEEEEEEEFFFDDD000000AAAFFFEEEFFFAAA888AAAAAA888AAAEEEEEEFFFDDD000000AAAFFFEEEFFFAAA888DDDEEEAAA888EEEEEEFFFDDD000000AAAFFFEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEFFFDDD000000AAAFFFEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEFFFDDD000000BBBFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEEE000000AAADDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDBBB000000000000000000000000000000000000000000000000000'

        rgb_image_data = []
        for pixel in chunk_str(image_data, 3):
            rgb_image_data.append(hex_to_rgb(double_mult(pixel)))

        img = Image.new('RGB', (16, 16), "black")  # create a new black image
        pixels = img.load()  # create the pixel map

        for i in range(img.size[0]):    # for every pixel:
            for j in range(img.size[1]):
                pixel = rgb_image_data[get_position(i, j)]
                # set the colour accordingly
                pixels[i, j] = (pixel[0], pixel[1], pixel[2])
        file_name = str(x) + "x" + str(y)
        img.save('images/' + str(x) + "x" + str(y) + ".png")

print 'Now finished!'
