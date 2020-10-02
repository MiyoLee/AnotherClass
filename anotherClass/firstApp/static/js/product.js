$(function(){
    $('.single-item').slick({
    dots:true,
    autoplay:true,
    autoplaySpeed: 3000,
    variableWidth: true,
    centerMode: true,
    centerPadding: '0px',
    prevArrow: '<span class="priv_arrow"><i class="fas fa-angle-left"></i></span>',
    nextArrow: '<span class="next_arrow"><i class="fas fa-angle-right"></i></span>',
    });
});

$(function(){
    $('.autoplay').slick({
    slidesToScroll: 1,
    autoplay: true,
    autoplaySpeed: 2000,
    variableWidth: true,
    centerMode: true,
    prevArrow: '<span class="priv_arrow"><i class="fas fa-angle-left"></i></span>',
    nextArrow: '<span class="next_arrow"><i class="fas fa-angle-right"></i></span>',
    });
});