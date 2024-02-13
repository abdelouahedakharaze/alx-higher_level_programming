#!/usr/bin/node
// Abdelouahed Akharaze

const Square = require('./5-square'); // Importing the Square class from 5-square.js

class Square1 extends Square { // Defining a subclass Square1 that extends the Square class
  charPrint (c) { // Defining a method charPrint that prints the square using the character c
    if (!c) // If c is not provided
    { this.print(); } // Call the print method from the parent class
    else {
      for (let i = 0; i < this.width; i++) // Iterate over the width of the square
      { console.log(c.repeat(this.height)); } // Print the character c repeated height times
    }
  }
}

module.exports = Square1; // Exporting the Square1 class for use in other files
