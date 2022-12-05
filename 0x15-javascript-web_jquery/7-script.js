// Fetches the name of a star wars character and displays it
$(function () {
  $.ajax({
    url: 'https://swapi-api.hbtn.io/api/people/5/?format=json',
    type: 'GET',
    dataType: 'json'
  }).done(function (character) {
    $('div#character').text(`${character.name}`);
  }).fail(function (xhr, status, error) {
    console.log('There was a problem');
    console.log(`Status: ${status}`);
    console.log(`Error: ${error}`);
    console.log(xhr);
  });
});
