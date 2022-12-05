// Fetches the names of all star wars movies and displays as a list on the page
$(function () {
  $.ajax({
    url: 'https://swapi-api.hbtn.io/api/films/?format=json',
    type: 'GET',
    dataType: 'json'
  }).done(function (result) {
    const movies = result.results;
    for (const x in movies) {
      $('ul#list_movies').append(`<li>${movies[x].title}</li>`);
    }
  }).fail(function (xhr, status, error) {
    console.log('There was a problem');
    console.log(`Status: ${status}`);
    console.log(`Error: ${error}`);
    console.log(xhr);
  });
});
