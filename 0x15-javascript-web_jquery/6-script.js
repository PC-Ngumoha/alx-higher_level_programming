// Change the header text dynamically on click.
$(function () {
  $('div#update_header').on('click', function () {
    $('header').text('New Header!!!');
  });
});
