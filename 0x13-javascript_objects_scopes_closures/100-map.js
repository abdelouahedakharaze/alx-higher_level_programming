#!/usr/bin/node
// Abdelouahed Akharaze
// Importing the list array from 100-data.js
const list = require('./100-data').list;

// Using the map function to compute a new array where each value is equal to the value of the initial list multiplied by its index
const newList = list.map((el, idx) => el * idx);

// Printing both the initial list and the new list
console.log(list);
console.log(newList);
