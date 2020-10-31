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
    slidesToShow: 4,
    autoplay: true,
    autoplaySpeed: 4000,
    infinite: false,
    prevArrow: '<span class="priv_arrow"><i class="fas fa-angle-left"></i></span>',
    nextArrow: '<span class="next_arrow"><i class="fas fa-angle-right"></i></span>',
    });
});

$(window).resize(function() {
  if ($(window).width() < 450) {
    $('.autoplay').slick('slickSetOption', 'slidesToShow', 1);
    $('.autoplay').css("width", '275px');
    $('.product-single').css("width", '80vw');
    $('.product-single').css("height", '60vw');
    $('.items').css("width", '80vw');
    $('.items img').css("width", '80vw');
    $('.items img').css("height", 'auto');
    $('.more-container img').css("width", '80vw');
    $('.more-container img').css("height", 'auto');
    $('.like').removeClass("like_block");
    $('.like').addClass("like_block_mb");
    $('.product-info').removeClass("product-info-o");
    $('.product-info').addClass("product-info-mb");
  }
  else{
    $('.autoplay').slick('slickSetOption', 'slidesToShow', 4);
    $('.autoplay').css("width", '');
    $('.like').addClass("like_block");
    $('.like').removeClass("like_block_mb");
    $('.product-info').addClass("product-info-o");
    $('.product-info').removeClass("product-info-mb");
  }
});

$(document).ready(function() {
  if ($(window).width() < 450) {
    $('.autoplay').slick('slickSetOption', 'slidesToShow', 1);
    $('.autoplay').css("width", '275px');
    $('.product-single').css("width", '80vw');
    $('.product-single').css("height", '60vw');
    $('.items').css("width", '80vw');
    $('.items img').css("width", '80vw');
    $('.items img').css("height", 'auto');
    $('.more-container img').css("width", '80vw');
    $('.more-container img').css("height", 'auto');
    $('.like').removeClass("like_block");
    $('.like').addClass("like_block_mb");
    $('.product-info').removeClass("product-info-o");
    $('.product-info').addClass("product-info-mb");
  }
  else{
    $('.autoplay').slick('slickSetOption', 'slidesToShow', 4);
    $('.autoplay').css("width", '');
    $('.like').addClass("like_block");
    $('.like').removeClass("like_block_mb");
    $('.product-info').addClass("product-info-o");
    $('.product-info').removeClass("product-info-mb");
  }
});