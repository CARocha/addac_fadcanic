
$(window).scroll(function() {
    if ($(".navbar").offset().top > 50) {
        $(".navbar-fixed-top").addClass("top-nav-collapse fondo");
        $(".navbar-fixed-top").removeClass("fondo2");
       
    } else {
        $(".navbar-fixed-top").removeClass("top-nav-collapse fondo");
        $(".navbar-fixed-top").addClass("fondo2");
    }
});


