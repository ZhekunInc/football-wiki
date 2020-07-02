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

  function myFunction() {
    if (document.getElementById("player-name").style.display == 'block') { 
        document.getElementById("player-name").style.display = "none";
    }
    else {
        document.getElementById("player-name").style.display = "block";
    }
  }

  $(document).ready(function() {
	$('.block').on('click', '.extremum-click', function() {
        $(this).siblings('.extremum-slide').slideToggle(0);
        $(this).siblings('.down-icon').slideToggle(0);
        $(this).siblings('.up-icon').slideToggle(1);
    });
});