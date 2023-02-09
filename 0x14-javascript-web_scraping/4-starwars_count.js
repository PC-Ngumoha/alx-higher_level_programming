#!/usr/bin/node
// Counts the number of star wars movies Wedge Antilles Has Starred in.
const process = require('process');
const request = require('request');

const actorUrl = 'https://swapi-api.alx-tools.com/api/people/18/';
const url = process.argv[2];

request.get(url, function (err, res, data) {
  if (!err) {
    const films = JSON.parse(data).results;
    console.log(films.reduce((count, film) => {
      return film.characters.find((character) => character.endsWith('/18/'))
	    ? count + 1
	    : count;
    }, 0));
  }
});
