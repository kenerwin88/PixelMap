// Each Pixel consists of an owner, color, and URL.
function Pixel(owner = 'Unowned', color = '#FFFFFF', url = '') {
  this.owner = owner;
  this.color = color;
  this.url = url;
}

// Initialize Grid
var grid = [[]]
for (var i = 0; i <= 1299; i++) {
  grid[i] = [];
}
for (var i = 0; i < 1299; i++) {
  for (var b = 0; b < 770; b++) {
    grid[i][b] = new Pixel;
  }
}

function convertHex(hex,opacity){
    hex = hex.replace('#','');
    this.r = parseInt(hex.substring(0,2), 16);
    g = parseInt(hex.substring(2,4), 16);
    b = parseInt(hex.substring(4,6), 16);
    result = {
      r: r,
      g: g,
      b: b,
      opacity: opacity/100
    }
    return result;
}

window.onload = function() {
    // Get the canvas and context
    var canvas = document.getElementById("viewport");
    var context = canvas.getContext("2d");

    // Define the image dimensions
    var width = canvas.width;
    var height = canvas.height;
    canvas.width = canvas.clientWidth;
    canvas.height = canvas.clientHeight;
    canvas.style.width = width; //actual width of canvas
    canvas.style.height = height; //actual height of canvas
    var mouseX = 0,
        mouseY = 0;
    canvas.addEventListener("mousemove", function(e) {
        var scrollX = (window.scrollX !== null && typeof window.scrollX !== 'undefined') ? window.scrollX : window.pageXOffset;
        var scrollY = (window.scrollY !== null && typeof window.scrollY !== 'undefined') ? window.scrollY : window.pageYOffset;
        mouseX = e.clientX;
        mouseY = e.clientY;
    }, false);
    canvas.addEventListener("click", function(evt) {
      var mousePos = getMousePos(canvas, evt);
      var message = 'Mouse position: ' + mousePos.x + ',' + mousePos.y + ' -- Owner: ' + grid[mousePos.x][mousePos.y].owner;
      window.location = grid[mousePos.x][mousePos.y].url;
    }, false);

    function getMousePos(canvas, evt) {
        var rect = canvas.getBoundingClientRect();
        return {
            x: Math.round(evt.clientX - rect.left),
            y: Math.round(evt.clientY - rect.top)
        };
    }
    var context = canvas.getContext('2d');

    canvas.addEventListener('mousemove', function(evt) {
        var mousePos = getMousePos(canvas, evt);
        var message = 'Mouse position: ' + mousePos.x + ',' + mousePos.y + ' -- Owner: ' + grid[mousePos.x][mousePos.y].owner;
        document.getElementById("myspan").textContent=message
    }, false);

    // Create an ImageData object
    var img = new Image();
    img.src = "bg.png";
    img.crossOrigin = "Anonymous"

    function setPixel(imageData, x, y, r, g, b, a) {
        index = (x + y * imageData.width) * 4;
        imageData.data[index + 0] = r;
        imageData.data[index + 1] = g;
        imageData.data[index + 2] = b;
        imageData.data[index + 3] = a;
    }
    img.onload = function() {
        context.drawImage(img, 0, 0);
        var imageData = context.getImageData(0, 0, 1299, 770);
        for (var i = 0; i < 1299; i++) {
          for (var b = 0; b < 770; b++) {
            if (grid[i][b].owner == 'Unowned') {}
            else {
              setPixel(imageData, i, b, convertHex(grid[i][b].color).r, convertHex(grid[i][b].color).g, convertHex(grid[i][b].color).b, 255);
            }
          }
        }

        setPixel(imageData, 15, 1, 255, 255, 255, 255); // 255 opaque
        context.putImageData(imageData, 0, 0);
    }
};
