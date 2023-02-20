/**
 * 3-script.js: Changes the color of the div#red_header to red when
 * the user clicks on it.
 */
$('div#toggle_header').on('click', function () {
  if ($('header').hasClass('green')) {
    $('header').removeClass('green').addClass('red');
  } else if ($('header').hasClass('red')) {
    $('header').removeClass('red').addClass('green');
  }
});
