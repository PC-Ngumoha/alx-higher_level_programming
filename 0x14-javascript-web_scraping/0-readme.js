#!/usr/bin/node
// prints the contents of a file to the console
const fs = require('fs');
const process = require('process');

const filename = process.argv[2];
if (filename !== null) {
  fs.readFile(filename, 'utf-8', (err, data) => {
    if (err) {
      console.log(err);
    } else {
      console.log(data);
    }
  });
}
