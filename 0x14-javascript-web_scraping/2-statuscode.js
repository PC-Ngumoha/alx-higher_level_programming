#!/usr/bin/node
// Makes a request to a url and prints the status code.
const process = require('process');
const request = require('request');

const url = process.argv[2];

request.get(url, function (err, res, data) {
  if (err) {
    console.log('code: ' + res.statusCode);
  } else {
    console.log('code: ' + res.statusCode);
  }
});
