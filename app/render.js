function preloadImages(srcs) {
    function loadImage(src) {
        return new Promise(function(resolve, reject) {
            var img = new Image();
            img.onload = function() {
                resolve(img);
            };
            img.onerror = img.onabort = function() {
                reject(src);
            };
            img.src = src;
        });
    }
    var promises = [];
    for (var i = 0; i < srcs.length; i++) {
        promises.push(loadImage(srcs[i]));
    }
    return Promise.all(promises);
}

window.onload = function() {
  imageNames = []
  for (var x = 0; x < 81; x++) {
    for (var y = 0; y < 49; y++) {
      imageNames.push("images/" + x + "x" + y + ".png")
    }
  }
  var context = document.getElementById('viewport').getContext("2d");
  preloadImages(imageNames).then(function(imgs) {
      // all images are loaded now and in the array imgs

      context.drawImage(imgs[0], 0, 0);
      context.drawImage(imgs[5], 16, 0);

  }, function(errImg) {
      // at least one image failed to load
  });

}
