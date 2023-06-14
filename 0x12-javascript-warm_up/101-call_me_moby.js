#!/usr/bin/node
exports.callMeMoby = function (x, theFunction) {
  let j = 1;
  while (j <= 3) {
    theFunction();
    j++;
  }
};
