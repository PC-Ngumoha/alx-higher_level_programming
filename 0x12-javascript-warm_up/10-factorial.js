#!/usr/bin/node

const process = require('process');
const number = parseInt(process.argv[2], 10);

function factorial (num) {
  if (isNaN(num)) return 1;
  if (num === 1) {
    return 1;
  } else {
    return (num * factorial(num - 1));
  }
}
console.log(factorial(number));
