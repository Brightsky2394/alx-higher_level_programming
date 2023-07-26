#!/usr/bin/node
const argv = process.argv;
const url = argv[2];
const request = require('request');
request(url,
  function (err, res, body) {
    if (err === null) {
      const rbody = JSON.parse(body);
      const dict = {};
      for (const j of rbody) {
        if (j.completed === true) {
          if (dict[j.userId] === undefined) { dict[j.userId] = 0; }
          dict[j.userId] += 1;
        }
      }
      console.log(dict);
    } else {
      console.log('error:', err);
    }
  });
