#!/usr/bin/node
const argv = process.argv;
const url = argv[2];
const request = require('request');
request(url, function (err, res, body) {
  if (err) {
    console.log(err);
  } else {
    const resBody = JSON.parse(body);
    const resDict = {};
    for (const i of resBody) {
      if (i.completed === true) {
        if (resDict[i.userId] === undefined) {
          resDict[i.userId] = 0;
        }
        resDict[i.userId] += 1;
      }
    }
    console.log(resDict);
  }
});
