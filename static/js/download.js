var href = location.href;
var prev = href.split("prev=")[1];
prev = prev.split("&")[0];
var file = href.split("file=")[1];

setInterval(function(){
    $(".counter").text(parseInt($(".counter").text())-1);
}, 1000);


setTimeout(function(){
    location.href = file;
    setTimeout(function(){
        location.href = prev;
    }, 1000);
}, 10000)