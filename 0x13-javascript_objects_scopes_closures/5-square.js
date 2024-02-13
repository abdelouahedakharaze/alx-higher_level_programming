#!/usr/bin/node
// Abdelouahed Akharaze

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    // Call the constructor of Rectangle with size as both width and height
    super(size, size);
  }
}

module.exports = Square;
