#!/usr/bin/node
// Prints out a list of characters in a particular star wars movie
const process = require('process');
const request = require('request');

const uri = `https://swapi-api.hbtn.io/api/films/${process.argv[2]}`;
request(uri, (err, res, output) => {
  if (err) {
    console.log(err);
  } else if (res.statusCode === 200) {
    const characters = JSON.parse(output).characters;
    displayCharacterNames(characters, 0);
  }
});

function displayCharacterNames (characters, index) {
  request(characters[index], (error, response, body) => {
    if (error) {
      console.log(error);
    } else if (response.statusCode !== 200) {
      console.log(`Error Occurred: ${response.statusCode}`);
    }
    console.log(JSON.parse(body).name);
    if (index + 1 < characters.length) {
      displayCharacterNames(characters, index + 1);
    }
  });
}
