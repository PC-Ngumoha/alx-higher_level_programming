#!/usr/bin/node
let list = require('./100-data.js').list;
console.log(list);
list = list.map((element, index) => element * index);
console.log(list);
