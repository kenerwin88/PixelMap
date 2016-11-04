var Web3 = require('web3');
var web3 = new Web3(new Web3.providers.HttpProvider("http://localhost:8546"));
console.log('Connected to Web3:', web3.isConnected());
var pixelmapContract = web3.eth.contract([{"constant":true,"inputs":[{"name":"","type":"uint256"}],"name":"owners","outputs":[{"name":"","type":"address"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"x","type":"uint256"},{"name":"y","type":"uint256"}],"name":"buyPixel","outputs":[{"name":"","type":"uint256"}],"payable":true,"type":"function"},{"constant":false,"inputs":[{"name":"x","type":"uint256"},{"name":"y","type":"uint256"}],"name":"getPos","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"","type":"uint256"}],"name":"urls","outputs":[{"name":"","type":"string"}],"payable":false,"type":"function"},{"constant":false,"inputs":[],"name":"getColors","outputs":[{"name":"","type":"uint256[1000230]"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"x","type":"uint256"},{"name":"y","type":"uint256"}],"name":"getPixel","outputs":[{"name":"","type":"address"},{"name":"","type":"string"},{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"x","type":"uint256"},{"name":"y","type":"uint256"},{"name":"color","type":"uint256"},{"name":"url","type":"string"},{"name":"price","type":"uint256"}],"name":"setPixel","outputs":[],"payable":false,"type":"function"},{"constant":false,"inputs":[],"name":"MEH","outputs":[],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"","type":"uint256"}],"name":"prices","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"","type":"uint256"}],"name":"colors","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[],"name":"getPrices","outputs":[{"name":"","type":"uint256[1000230]"}],"payable":false,"type":"function"}]);

var pixelmapContract = pixelmapContract.at('0x8939c3467dCC81C20f990558668807EFC892A02D');
var result = pixelmapContract.getColors.call();
//var result = web3.eth.getStorageAt("0xA0A4445e007361D484aF2c0e3837987f18fA07F2", 0);
//var result = pixelmapContract.owners;
//console.log(pixelmapContract.getPixel.call(2,0))
//console.log(result[1].c[0])
//console.log(result)
for (var i = 0, len = 1000230; i < len; i++) {
  if (result[i].c[0] == 88888) {console.log('hi')}
}
