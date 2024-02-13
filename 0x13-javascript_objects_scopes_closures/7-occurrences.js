#!/usr/bin/node
// Abdelouahed Akharaze
// Define the function nbOccurences which takes a list and a searchElement as arguments
exports.nbOccurences = function (list, searchElement) {
  // Initialize a variable count to count the occurrences
  let count = 0;

  // Iterate through the list
  for (let i = 0; i < list.length; i++) {
    // If the current element in the list is equal to the searchElement, increment count
    if (list[i] === searchElement) {
      count++;
    }
  }

  // Return the count of occurrences
  return count;
};
