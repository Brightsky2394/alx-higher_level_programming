#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/'.concat(process.argv[2]);

request(url, (err, res, body) => {
  if (err) console.log(err);
  JSON.parse(body).characters.forEach(character => {
    request(character, (err, res, body) => {
      if (!err) console.log(JSON.parse(body).name);
    });
  });
});
