#!/usr/bin/node
// Abdelouahed Akharaze

// Rectangle class definition
class Rectangle {
  // Constructor with two arguments: w (width) and h (height)
  constructor (w, h) {
    // Check if w or h is equal to 0 or not a positive integer
    if (w <= 0 || h <= 0 || isNaN(w) || isNaN(h)) {
      // If so, create an empty object
      return {};
    } else {
      // Otherwise, initialize instance attribute width with the value of w
      this.width = w;
      // Initialize instance attribute height with the value of h
      this.height = h;
    }
  }
}

// Exporting the Rectangle class to make it available for use in other files
module.exports = Rectangle;
