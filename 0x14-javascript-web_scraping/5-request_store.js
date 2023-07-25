#!/usr/bin/node
const args = process.argv;
const fd = require('fs');
const request = require('request');
const url = args[2];
const fileName = args[3];
request(url,
  (err, res, body) => {
    if (!err) {
      fd.writeFile(fileName, body, 'utf-8',
        err => {
          if (err) { console.log(err); }
        });
    } else {
      console.log('Error:', err);
    }
  });
