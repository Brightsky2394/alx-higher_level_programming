#!/usr/bin/node
const square5 = require('./5-square');
class Square extends square5 {
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
