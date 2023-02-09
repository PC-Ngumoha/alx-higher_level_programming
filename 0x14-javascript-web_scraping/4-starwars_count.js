#!/usr/bin/node
// Counts the number of star wars movies Wedge Antilles Has Starred in.
const process = require('process');
const request = require('request');

const actorUrl = 'https://swapi-api.alx-tools.com/api/people/18/';
const url = process.argv[2];

request.get(url, function (err, res, data) {
  if (!err) {
    let count = 0;
    const films = JSON.parse(data).results;
    films.forEach(function (film) {
      const characters = film.characters;
      characters.forEach(function (character) {
        if (character === actorUrl) count++;
      });
    });
    console.log(count);
  }
});
