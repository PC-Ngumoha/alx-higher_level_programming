/**
 * 8-script.js: List the titles of all movies gotten from the provided API.
 */
$.ajax({
  url: 'https://swapi-api.alx-tools.com/api/films/',
  data: {
    format: 'json'
  },
  type: 'GET',
  dataType: 'json'
}).done(function (data) {
  const movies = data.results;
  movies.forEach(movie => {
    $('ul#list_movies').append(`<li>${movie.title}</li>`);
  });
});
