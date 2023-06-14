#!/usr/bin/node
const Square5 = require('./5-square');

class Square extends Square5 {
  charPrint (c) {
    if (typeof (c) === 'undefined') {
      c = 'X';
    }
    let i = 0;
    while (i < this.height) {
      console.log(c.repeat(this.width));
      i++;
    }
  }
}

module.exports = Square;
