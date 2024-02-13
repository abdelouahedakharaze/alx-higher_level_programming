#!/usr/bin/node
// Define the function converter which takes a base as an argument
exports.converter = function (base) {
  // Return a function that converts a number from base 10 to the specified base
  return function (number) {
    // Use the toString method to convert the number to the specified base
    return number.toString(base);
  };
};
