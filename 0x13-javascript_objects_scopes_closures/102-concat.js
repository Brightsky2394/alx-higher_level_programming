#!/usr/bin/node
const args = process.argv;
const fs = require('fs');
const fileA = args[2];
const fileB = args[3];
const fileC = args[4];

const fileRead = (file) => {
  return new Promise((resolve, reject) => {
    fs.readFile(file, 'utf8', (err, data) => {
      if (err) {
        reject(err);
      } else {
        resolve(data);
      }
    });
  });
};

const promises = [fileA, fileB].map(fileRead);

Promise
  .all(promises)
  .then(resolve => {
    const Concat = resolve.join('');
    fs.writeFile(fileC, Concat, (err) => {
      if (err) throw err;
    });
  })
  .catch(err => console.log(err));
