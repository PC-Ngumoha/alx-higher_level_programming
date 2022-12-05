// Changes the color of the header sections contents
// when the div#red_header element is clicked
$(function () {
  $('div#toggle_header').on('click', function () {
    if ($('header').hasClass('green')) {
      $('header').removeClass('green');
      $('header').addClass('red');
    } else {
      $('header').removeClass('red');
      $('header').addClass('green');
    }
  });
});
