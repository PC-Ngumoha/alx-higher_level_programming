#!/usr/bin/node
// Gets the count of star wars movies where "Wedge Antilles" starred
// and displays said count on the console
// Wedge Antilles can be found in the 'characters' attribute array
// and is the person with the ID of 18.

const process = require('process');
const request = require('request');

request(process.argv[2], (error, response, body) => {
  if (!error) {
    const results = JSON.parse(body).results;
    console.log(
      results.reduce((count, movie) => {
        return movie.characters.find((character) => character.endsWith('/18/'))
          ? count + 1
          : count;
      }, 0)
    );
  }
});
