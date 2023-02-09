#!/usr/bin/node
// Gets the contents of a web page and store in a file.
const fs = require('fs');
const process = require('process');
const request = require('request');

request.get(process.argv[2])
  .on('error', (err) => console.log(err))
  .pipe(fs.createWriteStream(process.argv[3]));
