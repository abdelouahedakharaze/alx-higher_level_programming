#!/usr/bin/node
// Abdelouahed Akharaze

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    } else {
      return {}; // Return an empty object if w or h is not a positive integer
    }
  }

  // Instance method print() to print the rectangle using the character 'X'
  print () {
    for (let i = 0; i < this.height; i++) {
      let row = '';
      for (let j = 0; j < this.width; j++) {
        row += 'X';
      }
      console.log(row);
    }
  }

  // Instance method rotate() to exchange the width and the height of the rectangle
  rotate () {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  // Instance method double() to multiply the width and the height of the rectangle by 2
  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
