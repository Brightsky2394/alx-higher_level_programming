#!/usr/bin/node
const args = process.argv;
const url = args[2];
const request = require('request');
request(url, (err, res, body) => {
  if (!err) {
    const resBody = JSON.parse(body);
    const resDict = {};
    for (const j of resBody) {
      if (j.completed === true) {
        if (resDict[j.userId] === undefined) { resDict[j.userId] = 0; } else { resDict[j.userId] += 1; }
      }
    }
    console.log(resDict);
  } else {
    console.log('Error:', err);
  }
});
