#!/usr/bin/node

const process = require('process');
const size = parseInt(process.argv[2], 10);

if (isNaN(size)) {
  console.log('Missing size');
} else {
  let square = '';
  for (let i = 0; i < size; i++) {
    for (let j = 0; j < size; j++) {
      square += 'X';
    }
    if (i < size - 1) square += '\n';
  }
  console.log(square);
}
