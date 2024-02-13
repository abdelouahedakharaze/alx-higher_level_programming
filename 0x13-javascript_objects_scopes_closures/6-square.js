#!/usr/bin/node
// Abdelouahed Akharaze

// Importing the Square class from 5-square.js
// Defining a subclass Square1 that extends the Square class
// Defining a method charPrint that prints the square using the character c
// If c is not provided, call the print method from the parent class
// Otherwise, print the character c repeated height times
// Exporting the Square1 class for use in other files
const Square = require('./5-square');

class Square1 extends Square {
  charPrint (c) {
    if (!c) this.print();
    else {
      for (let i = 0; i < this.width; i++) console.log(c.repeat(this.height));
    }
  }
}

module.exports = Square1;
