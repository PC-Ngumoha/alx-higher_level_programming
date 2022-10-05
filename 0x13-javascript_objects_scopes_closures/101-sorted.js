#!/usr/bin/node
const dict = require('./101-data.js').dict;
const newDict = {};
let occurences = [];
let sortable = [];

// create an array from the dict
for (const user in dict) {
  sortable.push([[user], dict[user]]);
}

// determine the max occurrence
for (let i = 0; i < sortable.length; i++) {
  occurences.push(sortable[i][1]);
}
occurences = new Set(occurences); // creates a new set from the 'occurences' array

// sort the array
sortable.sort((a, b) => {
  return a[1] - b[1];
});

// concatenate arrays with same distribution numbers
const compressed = [];
for (const occur of occurences) {
  compressed[occur - 1] = [occur, []];
  for (let i = 0; i < sortable.length; i++) {
    if (occur === sortable[i][1]) {
      compressed[occur - 1][1] = compressed[occur - 1][1].concat(sortable[i][0]);
    }
  }
}
sortable = compressed;

// Assign sorted array to the new dictionary
sortable.forEach((element) => {
  newDict[element[0]] = element[1];
});

// Prints out the new dictionary
console.log(newDict);
