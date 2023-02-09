#!/usr/bin/node
// A program to read a file
const fs = require('fs');
const process = require('process');

const filename = process.argv[2];

fs.readFile(filename, 'utf-8', function (err, data) {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});
