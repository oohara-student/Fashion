$(function () {
    $('select').change(function () {
      var adjust = 133;
      var speed = 400;
      var href = $(this).val();
      var target = $(href == "#" || href == "" ? 'html' : href);
      var position = target.offset().top - adjust;;
      $('body,html').animate({scrollTop:position}, speed, 'swing');
      return false;
    });
  });