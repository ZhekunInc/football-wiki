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

var swiper = new Swiper('.swiper-container', {
    effect: 'cube',
    grabCursor: true,
    lazy: true,
    cubeEffect: {
      shadow: true,
      slideShadows: true,
      shadowOffset: 20,
      shadowScale: 0.94,
    },
    autoplay: {
        delay: 2500,
        disableOnInteraction: false,
    },
    loop: true,
    pagination: {
      el: '.swiper-pagination',
    },
  });

    function zero_first_format(value)
    {
        if (value < 10)
        {
            value='0'+value;
        }
        return value;
    }
    function date_time()
    {
        var current_datetime = new Date();
        var day = zero_first_format(current_datetime.getDate());
        var month = zero_first_format(current_datetime.getMonth()+1);
        var year = current_datetime.getFullYear();
        var hours = zero_first_format(current_datetime.getHours());
        var minutes = zero_first_format(current_datetime.getMinutes());
        var seconds = zero_first_format(current_datetime.getSeconds());

        return day+"."+month+"."+year+" "+hours+":"+minutes+":"+seconds;
    }


    setInterval(function () {
      document.getElementById('date-time').innerHTML = date_time();
  }, 1000);