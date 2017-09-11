function setTileHeight() {
    $(".tile").each(function() {
        width = $(this).width();
        $(this).height(width);
    });
}

$(document).ready(function() {
    setTileHeight();
});

$(window).resize(function() {
    setTileHeight();
});
