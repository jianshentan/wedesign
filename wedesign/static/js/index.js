function set_tile_height() {
    $(".tile").each(function() {
        width = $(this).width();
        $(this).height(width);
    });
}

/**
 ** Shuffles array in place. ES6 version
 ** @param {Array} a items The array containing the items.
 **/
function shuffle(a) {
    for (let i = a.length; i; i--) {
        let j = Math.floor(Math.random() * i);
        [a[i - 1], a[j]] = [a[j], a[i - 1]];
    }
}

function load_images(urls) {
    var tile_container = $("#tiles");
    shuffle(urls);

    // max_tiles, mt, is defined: mt = (n * 4) - 1
    max_tiles = 27; 

    for (i in urls) {
        var url = urls[i];
        tile = $("<div class='tile'><img src='/assets/images/" + url + "/'></div>");
        tile_container.append(tile);
        if (i >= max_tiles) {
            break;
        }
    }
}

$(document).ready(function() {
    load_images(imgs_url);
    set_tile_height();

    // need to run again for some reason...
    setTimeout(set_tile_height, 100);
});

$(window).resize(function() {
    set_tile_height();
});
