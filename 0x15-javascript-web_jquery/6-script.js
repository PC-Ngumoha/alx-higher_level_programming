/**
 * 6-script.js: Changes the text content of the header tag in response to
 * user clicks.
 */
$('div#update_header').on('click', function () {
  $('header').text('New Header!!!');
});
