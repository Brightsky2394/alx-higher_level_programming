#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h >= 1) {
      this.width = w;
      this.height = h;
    }
  }
}

module.exports = Rectangle;
