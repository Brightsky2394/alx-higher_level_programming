#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h >= 1) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let i;
    const len = this.height;
    i = 0;
    while (i < len) {
      console.log('X'.repeat(this.width));
      i++;
    }
  }
}

module.exports = Rectangle;
