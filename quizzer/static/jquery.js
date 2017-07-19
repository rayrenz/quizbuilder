$(document).ready(function (){
    var height = $(window).height() - 80;
    $("#main").height(height);
});

window.onresize = function(event) {
    var height = $(window).height() - 80;
    $("#main").height(height);
}