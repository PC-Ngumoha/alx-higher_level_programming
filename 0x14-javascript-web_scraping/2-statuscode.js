#!/usr/bin/node
// Prints the status code of a the response from the query to the specified uri
const process = require('process');
const request = require('request');

const url = process.argv[2];
if (url !== null) {
  request(url, (error, response, body) => {
    if (error) console.log(error);
    console.log(`code: ${response.statusCode}`);
  });
}
