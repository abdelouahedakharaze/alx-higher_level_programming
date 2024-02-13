#!/usr/bin/node
// Abdelouahed Akharaze
const fs = require('fs');

// Extracting file paths from command line arguments
const [, , fileA, fileB, fileC] = process.argv;

// Reading the contents of fileA
fs.readFile(fileA, 'utf8', (err, dataA) => {
  if (err) {
    console.error(err);
    return;
  }

  // Reading the contents of fileB
  fs.readFile(fileB, 'utf8', (err, dataB) => {
    if (err) {
      console.error(err);
      return;
    }

    // Concatenating the contents of fileA and fileB
    const concatenatedContent = `${dataA}${dataB}`;

    // Writing the concatenated content to fileC
    fs.writeFile(fileC, concatenatedContent, err => {
      if (err) {
        console.error(err);
        return;
      }

      console.log('Concatenation successful!');
    });
  });
});
