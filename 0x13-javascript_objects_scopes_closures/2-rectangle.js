#!/usr/bin/node

// Abdelouahed Akharaze

class Rectangle {
  constructor (w, h) {
    // Check if both width (w) and height (h) are positive integers

    if (w > 0 && h > 0) {
      // If so, initialize width and height attributes
      this.width = w;
      this.height = h;
    }
  }
}

module.exports = Rectangle;
