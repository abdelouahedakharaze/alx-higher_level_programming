#!/usr/bin/node
// Abdelouahed Akharaze

const SquareParent = require('./5-square');

class Square extends SquareParent {
  constructor (size) {
    // Call the constructor of SquareParent with size as the argument
    super(size);
  }

  charPrint (c) {
    // If c is undefined, use 'X' as the default character
    if (c === undefined) {
      c = 'X';
    }

    // Print the square using the character c
    for (let i = 0; i < this.height; i++) {
      console.log(c.repeat(this.width));
    }
  }
}

module.exports = Square;
