#!/usr/bin/node
const args = process.argv;
const fileName = args[2];
const str = args[3];
const fd = require('fs');
fd.writeFile(fileName, str, 'utf-8',
  err => {
    console.log(err);
  });
