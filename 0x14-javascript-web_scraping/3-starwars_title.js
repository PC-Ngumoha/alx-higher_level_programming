#!/usr/bin/node
// Gets the title of a specific star wars movie.
const process = require('process');
const request = require('request');

const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;

request.get(url, function (err, res, data) {
  if (!err) {
    data = JSON.parse(data);
    console.log(data.title);
  }
});
