#!/usr/bin/node
const args = process.argv;
const id = args[2];
const url = 'https://swapi-api.alx-tools.com/api/films/'.concat(id);
const request = require('request');
request(url,
  (err, res, body) => {
    if (!err) {
      const resBody = JSON.parse(body);
      console.log(resBody.title);
    } else {
      console.log(err);
    }
  });
