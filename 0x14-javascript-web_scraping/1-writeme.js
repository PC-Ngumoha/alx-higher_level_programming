#!/usr/bin/node
// Writes to a file.
const fs = require('fs');
const process = require('process');

const filename = process.argv[2];
const data = process.argv[3];

fs.writeFile(filename, data, 'utf-8', function (err) {
  if (err) {
    console.log(err);
  }
});
