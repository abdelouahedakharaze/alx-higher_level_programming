#!/usr/bin/node
// Abdelouahed Akharaze
// Importing the file system module
const fs = require('fs');

// Extracting command line arguments
const argv = process.argv;

// Reading the contents of the first source file synchronously
const file1 = fs.readFileSync(argv[2], 'utf-8').toString();

// Reading the contents of the second source file synchronously
const file2 = fs.readFileSync(argv[3], 'utf-8').toString();

// Concatenating the contents of the two files
const concatenatedContent = file1 + file2;

// Writing the concatenated content to the destination file synchronously
fs.writeFileSync(argv[4], concatenatedContent);
