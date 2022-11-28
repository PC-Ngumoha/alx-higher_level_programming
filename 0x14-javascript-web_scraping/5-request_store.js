#!/usr/bin/node
// Pipes the contents of a website into a local file/buffer
const process = require('process');
const request = require('request');
const fs = require('fs');

const uri = process.argv[2];
const destFile = process.argv[3];
// Streams the response into a file
request
  .get(uri)
  .on('error', function (err) {
    console.log(err);
  })
  .pipe(fs.createWriteStream(destFile));
