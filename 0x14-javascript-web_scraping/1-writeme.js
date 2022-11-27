#!/usr/bin/node
// Writes to a file on the file system.
const fs = require('fs');
const process = require('process');

const filename = process.argv[2];
const data = process.argv[3];

if (filename !== null) {
  fs.writeFile(filename, data, 'utf-8', (err) => {
    if (err) console.log(err);
  });
}
