pragma solidity ^0.4.3;
contract MEH {
    mapping (uint => address) owners;
    mapping (uint => string) colors;
    mapping (uint => string) urls;
    mapping (uint => uint) prices;
    address creator;

    // Constructor
    function MEH() {
        creator = msg.sender;
    }
    // Given X & Y, return pixel number.
    function getPos(uint x, uint y) returns (uint) {
        return y*1000+x;
    }

    // Get Pixel information at X,Y position.
    function getPixel(uint x, uint y) returns (address, string, string) {
        uint location = getPos(x, y);
        return (owners[location], urls[location], colors[location]);
    }

    // Purchase an unclaimed Pixel for 0.1Eth.
    function buyPixel(uint x, uint y) payable returns (uint) {
        uint location = getPos(x, y);
        uint price = 100000000000000000;
        if (owners[location] == msg.sender) {
            throw; // You already own this pixel silly!
        }
        // If Unowned by the Bank
        if (owners[location] == 0x0) {
            if (msg.value == 100000000000000000) {
                // Send to Creator
                if (creator.send(100000000000000000)) {
                    owners[location] = msg.sender;
                    prices[location] = 0; // Set Price to 0.  0 is not for sale.
                }
                else {throw;}
            }
            else {
                throw; // 0.1eth not supplied
            }
        }
        else {
            if (owners[location] != 0x0) {
                price = prices[location];
                if (price == 0) {throw;} // Pixel not for sale!
                else {
                    if (msg.value == price) {
                        if (owners[location].send(price)) {
                            // Set New Owner
                            owners[location] = msg.sender;
                            prices[location] = 0; // Set Price to 0.
                        }
                        else {throw;}
                    }
                }
            }
        }
    }

    // Set an already owned Pixel to whatever you'd like.
    function setPixel(uint x, uint y, string color, string url, uint price) {
        uint location = getPos(x, y);
        if (owners[location] != msg.sender) {throw;} // Pixel not owned by you!
        else {
            colors[location] = color;
            urls[location] = url;
            prices[location] = price;
        }
    }

}
