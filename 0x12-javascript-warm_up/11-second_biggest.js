#!/usr/bin/node

const process = require('process');
const numbers = [];
let i;

for (i = 2; i < process.argv.length; i++) {
  numbers.push(parseInt(process.argv[i], 10));
}

const listLength = numbers.length;

if (listLength <= 1) {
  console.log(0);
} else {
  let secondBest;
  const best = Math.max(...numbers);
  secondBest = 0;
  for (i = 0; i < listLength; i++) {
    if ((numbers[i] > secondBest) && (numbers[i] !== best)) {
      secondBest = numbers[i];
    }
  }
  console.log(secondBest);
}
