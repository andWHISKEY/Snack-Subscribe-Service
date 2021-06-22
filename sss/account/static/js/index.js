jQuery(document).ready(function ($) {
  $(".scroll").click(function (event) {
    event.preventDefault();
    $("html,body").animate({ scrollTop: $(this.hash).offset().top }, 500);
  });
});

$(document).ready(function(){
    $("#login1").click(function(){
      $("#card").fadeIn(500);
      $("#login1").fadeOut(500);
    });
  });