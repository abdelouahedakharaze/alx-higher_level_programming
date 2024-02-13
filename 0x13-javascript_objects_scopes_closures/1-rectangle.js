#!/usr/bin/node
// Abdelouahed Akharaze

// Rectangle class definition
class Rectangle {
  // Constructor with two arguments: w (width) and h (height)
  constructor (w, h) {
    // Initialize instance attribute width with the value of w
    this.width = w;
    // Initialize instance attribute height with the value of h
    this.height = h;
  }
}

// Exporting the Rectangle class to make it available for use in other files
module.exports = Rectangle;
