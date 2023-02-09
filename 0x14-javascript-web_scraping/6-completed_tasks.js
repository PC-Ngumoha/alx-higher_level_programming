#!/usr/bin/node
// Displays number of tasks completed by userId
const process = require('process');
const request = require('request');

const url = process.argv[2];

request.get(url, (err, res, data) => {
  if (!err) {
    const tasks = JSON.parse(data);
    const output = {};

    tasks.forEach((task) => {
      if (task.completed === true) {
        (output[task.userId] === undefined)
          ? output[task.userId] = 1
          : output[task.userId] += 1;
      }
    });
    console.log(output);
  }
});
