$(function(){
    $('.single-item').slick({
    dots:true,
    autoplay:true,
    autoplaySpeed: 3000,
    variableWidth: true,
    centerPadding: '0px',
    prevArrow: '<span class="priv_arrow"><i class="fas fa-angle-left"></i></span>',
    nextArrow: '<span class="next_arrow"><i class="fas fa-angle-right"></i></span>',
    });
});
$(function(){
    $('.autoplay').slick({
    slidesToScroll: 1,
    slidesToShow: 3,
    autoplay: true,
    autoplaySpeed: 4000,
    infinite: false,
    prevArrow: '<span class="priv_arrow"><i class="fas fa-angle-left"></i></span>',
    nextArrow: '<span class="next_arrow"><i class="fas fa-angle-right"></i></span>',
    });
});

$(window).resize(function() {
  if ($(window).width() < 450) {
    $('.autoplay').slick('slickSetOption', 'slidesToShow', 2);

  }
  else{
    $('.autoplay').slick('slickSetOption', 'slidesToShow', 3);

  }
});

$(document).ready(function() {
  if ($(window).width() < 450) {
    $('.autoplay').slick('slickSetOption', 'slidesToShow', 2);

  }
  else{
    $('.autoplay').slick('slickSetOption', 'slidesToShow', 3);

  }
});