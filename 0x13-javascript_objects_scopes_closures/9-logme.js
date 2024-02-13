#!/usr/bin/node
// Abdelouahed Akharaze
// Define the function logMe which takes an item as an argument
exports.logMe = function (item) {
  // Define a variable to keep track of the number of arguments already printed
  if (this.count === undefined) {
    this.count = 0;
  }

  // Print the number of arguments already printed and the current argument value
  console.log(this.count + ': ' + item);

  // Increment the count of arguments already printed
  this.count++;
};
