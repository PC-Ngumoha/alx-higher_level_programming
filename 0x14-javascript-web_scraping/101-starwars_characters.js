#!/usr/bin/node
// Prints the name of all actors that starred a star wars movie
const process = require('process');
const request = require('request');

const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;

request.get(url, (err, res, data) => {
  if (!err) {
    const characters = JSON.parse(data).characters;
    printName(characters, 0);
  }
});

function printName (characters, index) {
  request.get(characters[index], (err, res, data) => {
    if (!err) {
      console.log(JSON.parse(data).name);
      if (index + 1 < characters.length) {
        printName(characters, index + 1);
      }
    }
  });
}
