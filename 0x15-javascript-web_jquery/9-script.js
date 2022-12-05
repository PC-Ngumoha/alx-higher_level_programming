// Fetches some data from the hello API and displays it's value on the screen.

$(function () {
  $.get('https://fourtonfish.com/hellosalut/?lang=fr', (data, status) => {
    $('div#hello').text(data.hello);
  });
});
