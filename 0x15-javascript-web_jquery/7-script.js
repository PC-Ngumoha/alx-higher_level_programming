/**
 * 7-script.js: Gets the name of a starwars actor from the API.
 */
$.ajax({
  url: 'https://swapi-api.alx-tools.com/api/people/5/',
  data: {
    format: 'json'
  },
  type: 'GET',
  dataType: 'json'
}).done(function (star) {
  $('div#character').text(star.name);
});
