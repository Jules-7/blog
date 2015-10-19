$(document).ready(function(){
    // posts slider
    $('.posts_slide').slick({
        autoplay: true,
        autoplaySpeed: 3000,
        infinite: true,
        slidesToShow: 1,
        slidesToScroll: 1,
        dots: true
    });


    function apply_tags_freq() {
        $(".tag").each(function() {
            var freq = $(this).data("freq");
            if (freq < 2){
                $(this).find('a').addClass('small_freq');
            } else {
                $(this).find('a').addClass('big_freq');
            }
        });
    }

    apply_tags_freq();


});
