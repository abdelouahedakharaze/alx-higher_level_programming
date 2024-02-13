#!/usr/bin/node
// Abdelouahed Akharaze
// Importing the dict object from 101-data.js
const dict = require('./101-data').dict;

// Initializing an empty object to store the new dictionary
const occurrencesById = {};

// Looping through the keys (user ids) of the original dictionary
for (const userId in dict) {
  // Getting the number of occurrences for the current user id
  const occurrences = dict[userId];

  // Checking if the occurrences value is already a key in the new dictionary
  if (!occurrencesById[occurrences]) {
    // If not, initialize it with an empty array
    occurrencesById[occurrences] = [];
  }

  // Pushing the user id to the list of user ids for the current number of occurrences
  occurrencesById[occurrences].push(userId);
}

// Printing the new dictionary
console.log(occurrencesById);
