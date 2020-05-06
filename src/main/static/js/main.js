$("document").ready(function($){
    var nav = $('.js-scrollTop');

    $(window).scroll(function () {
        if ($(this).scrollTop() > 170) {
            nav.addClass("anchor");
        } else {
            nav.removeClass("anchor");
        }
    });
});

$('#js-up').click(function() {
    $('body,html').animate({ scrollTop:0 },500);
    return false;
  })