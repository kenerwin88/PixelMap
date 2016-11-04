import json
from web3 import Web3, KeepAliveRPCProvider, IPCProvider
web3 = Web3(KeepAliveRPCProvider(host='localhost', port='8546'))
print(web3.isConnected())
abi = json.loads('[{"constant":true,"inputs":[{"name":"","type":"uint256"}],"name":"owners","outputs":[{"name":"","type":"address"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"x","type":"uint256"},{"name":"y","type":"uint256"}],"name":"buyPixel","outputs":[{"name":"","type":"uint256"}],"payable":true,"type":"function"},{"constant":false,"inputs":[{"name":"x","type":"uint256"},{"name":"y","type":"uint256"}],"name":"getPos","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"","type":"uint256"}],"name":"urls","outputs":[{"name":"","type":"string"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"x","type":"uint256"},{"name":"y","type":"uint256"}],"name":"getPixel","outputs":[{"name":"","type":"address"},{"name":"","type":"string"},{"name":"","type":"string"}],"payable":false,"type":"function"},{"constant":false,"inputs":[],"name":"MEH","outputs":[],"payable":false,"type":"function"},{"constant":false,"inputs":[],"name":"getOwners","outputs":[{"name":"","type":"address[1000230]"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"","type":"uint256"}],"name":"prices","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"","type":"uint256"}],"name":"colors","outputs":[{"name":"","type":"string"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"x","type":"uint256"},{"name":"y","type":"uint256"},{"name":"color","type":"string"},{"name":"url","type":"string"},{"name":"price","type":"uint256"}],"name":"setPixel","outputs":[],"payable":false,"type":"function"}]')
contract = web3.eth.contract(abi, address="0xc016c69e10962585ad4b1f5557c00a2b7c92891b")

#for i in range(1299): #1299
#    for b in range(770): #770
#        moo = contract.call().getPixel(i, b)#
#x = contract.call().getOwners()[0]
x = contract.getOwner()
print x
print 'finishe'
