#!/usr/bin/node
// Abdelouahed Akharaze

// Importing the Square class from 5-square.js
const Square = require('./5-square');

// Defining a subclass Square1 that extends the Square class
class Square1 extends Square {
  // Defining a method charPrint that prints the square using the character c
  charPrint (c) {
    // If c is not provided, call the print method from the parent class
    if (!c) { this.print(); }

    // Otherwise, print the character c repeated height times
    else {
      for (let i = 0; i < this.width; i++) { console.log(c.repeat(this.height)); }
    }
  }
}

// Exporting the Square1 class for use in other files
module.exports = Square1;
