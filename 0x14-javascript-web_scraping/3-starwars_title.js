#!/usr/bin/node
// Displays the title of star wars shows fetched from the API
const process = require('process');
const request = require('request');

const id = parseInt(process.argv[2], 10);
if (!isNaN(id)) {
  const uri = `https://swapi-api.hbtn.io/api/films/${id}`;
  request(uri, (error, response, body) => {
    if (error) console.log(error);
    const data = JSON.parse(body);
    console.log(data.title);
  }); 
}
