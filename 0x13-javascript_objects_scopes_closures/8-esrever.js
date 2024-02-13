#!/usr/bin/node
// Abdelouahed Akharaze
// Define the function esrever which takes a list as an argument
exports.esrever = function (list) {
  // Initialize an empty array to store the reversed list
  const reversedList = [];

  // Iterate through the original list in reverse order
  for (let i = list.length - 1; i >= 0; i--) {
    // Push each element of the original list into the reversed list
    reversedList.push(list[i]);
  }

  // Return the reversed list
  return reversedList;
};
