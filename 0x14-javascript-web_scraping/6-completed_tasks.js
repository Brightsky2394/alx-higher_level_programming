#!/usr/bin/node
const apiUrl = process.argv[2];
const request = require('request');
request(apiUrl, (err, res, body) => {
  if (err === null) {
    const completedUserById = {};
    JSON.parse(body).forEach(i => {
      const userId = i.userId;
      const completed = i.completed;
      if (completed && completedUserById[userId] === undefined) { completedUserById[userId] = 0; }
      if (completed) { completedUserById[userId]++; }
    });
    console.log(completedUserById);
  } else { throw err; }
});
