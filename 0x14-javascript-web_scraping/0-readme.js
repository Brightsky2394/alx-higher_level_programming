#!/usr/bin/node
const args = process.argv;
const fileName = args[2];
const file = require('fs');
file.readFile(fileName, 'utf-8',
  (err, data) => {
    if (err) { console.log(err); } else { process.stdout.write(data); }
  });
