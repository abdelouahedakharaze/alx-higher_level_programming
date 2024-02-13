#!/usr/bin/node
// Abdelouahed Akharaze
// Import the list array from 100-data.js
const { list } = require('./100-data');

// Use the map function to compute a new array where each value is equal to the value of the initial list multiplied by the index in the list
const newList = list.map((value, index) => value * index);

// Print both the initial list and the new list
console.log(list);
console.log(newList);
