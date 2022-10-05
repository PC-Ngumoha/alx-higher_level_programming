#!/usr/bin/node
const process = require('process');
const fs = require('fs');

if (process.argv.length === 5) {
  const fileA = process.argv[2];
  const fileB = process.argv[3];
  const fileC = process.argv[4];
  let content1;
  let content2;
  // reading the contents of fileA
  content1 = fs.readFileSync(fileA, 'utf-8');
  // reading the contents of fileB
  content2 = fs.readFileSync(fileB, 'utf-8');

  // concatenating the content from both files
  const result = content1.concat(content2);
  // writing the result to the destination file (fileC)
  fs.writeFile(fileC, result, (err) => {
    if (err) throw err;
  });
}
