#!/usr/bin/node
const args = process.argv;
const request = require('request');
const url = args[2];
request(url,
  (err, res) => {
    if (!err) { process.stdout.write(`code: ${res.statusCode}`); } else { console.error('Error:', err); }
  });
