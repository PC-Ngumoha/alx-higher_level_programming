/**
 * 3-script.js: Changes the color of the div#red_header to red when
 * the user clicks on it.
 */
$('div#red_header').on('click', function () {
  $('header').addClass('red');
});
