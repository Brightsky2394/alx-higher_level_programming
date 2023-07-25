#!/usr/bin/node
const args = process.argv;
const request = require('request');
const url = args[2];
const id = 18;
request(url,
  (err, res, body) => {
    if (!err) {
      const resBody = JSON.parse(body);
      let count = 0;
      for (const j of resBody.results) {
        for (const i of j.characters) {
          if (i.search(id) > 0) { count = count + 1; }
        }
      }
      console.log(count);
    } else {
      console.log('Error:', err);
    }
  });
