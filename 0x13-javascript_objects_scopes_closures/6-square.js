#!/usr/bin/node
const square_ = require('./5-square');
class Square extends square_ {
  charPrint (c) {
    if (typeof (c) === 'undefined') {
      c = 'X';
    } else {
      let i = 0;
      while (i < this.height) {
        console.log(c.repeat(this.width));
        i++;
      }
    }
  }
}

module.exports = Square;
