import json
from web3 import Web3, KeepAliveRPCProvider, IPCProvider
from PIL import Image

web3 = Web3(KeepAliveRPCProvider(host='localhost', port='8546'))
print(web3.isConnected())
abi = json.loads('[{"constant":true,"inputs":[{"name":"","type":"uint256"}],"name":"owners","outputs":[{"name":"","type":"address"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"x","type":"uint256"},{"name":"y","type":"uint256"}],"name":"buyTile","outputs":[],"payable":true,"type":"function"},{"constant":false,"inputs":[{"name":"x","type":"uint256"},{"name":"y","type":"uint256"}],"name":"getPos","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"","type":"uint256"}],"name":"urls","outputs":[{"name":"","type":"string"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"x","type":"uint256"},{"name":"y","type":"uint256"}],"name":"getTile","outputs":[{"name":"","type":"address"},{"name":"","type":"string"},{"name":"","type":"string"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"","type":"uint256"}],"name":"images","outputs":[{"name":"","type":"string"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"","type":"uint256"}],"name":"prices","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"x","type":"uint256"},{"name":"y","type":"uint256"},{"name":"image","type":"string"},{"name":"url","type":"string"},{"name":"price","type":"uint256"}],"name":"setPixel","outputs":[],"payable":false,"type":"function"},{"inputs":[],"type":"constructor"}]')

contract = web3.eth.contract(
    abi, address="0x1468804F7dC7020823defd910C5709C7B93fe295")
tile = contract.call().getTile(2, 1)

image_data = tile[2]
if not image_data:
    image_data = '000000000000000000000000000000000000000000000000000777AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABBBAAA000000AAAFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFDDD000000AAAFFFFFFEEEEEEEEEEEEEEEEEEEEEEEEEEEFFFDDD000000AAAFFFEEEEEEFFFFFFEEEEEEFFFFFFEEEEEEFFFDDD000000AAAFFFEEEFFFAAA999DDDEEEAAAAAAEEEEEEFFFDDD000000AAAFFFEEEFFF999777BBBBBB888888EEEEEEFFFDDD000000AAAFFFEEEEEEDDDBBB888888AAADDDEEEEEEFFFDDD000000AAAFFFEEEEEEEEEBBB888777AAAEEEEEEEEEFFFDDD000000AAAFFFEEEFFFAAA888AAAAAA888AAAEEEEEEFFFDDD000000AAAFFFEEEFFFAAA888DDDEEEAAA888EEEEEEFFFDDD000000AAAFFFEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEFFFDDD000000AAAFFFEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEFFFDDD000000BBBFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEEE000000AAADDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDBBB000000000000000000000000000000000000000000000000000'
print image_data
