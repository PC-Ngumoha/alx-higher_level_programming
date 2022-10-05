#!/usr/bin/node

exports.logMe = function log (item) {
  if (typeof log.count == 'undefined') log.count = 0;
  console.log(`${log.count}: ${item}`);
  log.count++;
};
