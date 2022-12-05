// Changes the color of the header sections contents
// when the div#red_header element is clicked
$(function () {
  $('div#red_header').on('click', function () {
    $('header').addClass('red');
  });
});
