#!/usr/bin/node

const process = require('process');
const numTimes = parseInt(process.argv[2], 10);

if (isNaN(numTimes)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < numTimes; i++) {
    console.log('C is fun');
  }
}
