#!/usr/bin/node

const process = require('process');
const cmdLength = process.argv.length;

if (cmdLength <= 2) {
  console.log('No argument');
} else if (cmdLength === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
