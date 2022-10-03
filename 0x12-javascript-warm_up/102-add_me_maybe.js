#!/usr/bin/node
exports.addMeMaybe = function (a, func) {
  a++;
  func(a);
};
