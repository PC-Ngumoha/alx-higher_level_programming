/**
 * 9-script.js: Gets data from an external API
 */
$(function () {
  $.get('https://fourtonfish.com/hellosalut/?lang=fr', function (data) {
    $('div#hello').text(data.hello);
  });
});
