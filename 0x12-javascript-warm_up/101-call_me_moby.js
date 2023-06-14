#!/usr/bin/node
exports.callMeMoby = function (x, theFunction) {
  let j = 1;
  while (j <= x) {
    theFunction();
    j++;
  }
};
