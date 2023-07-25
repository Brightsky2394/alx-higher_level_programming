#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
request(url, (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    const completedTasksByUsers = {};
    const resBody = JSON.parse(body);
    for (let i = 0; i < resBody.length; i++) {
      const userId = resBody[i].userId;
      const completed = resBody[i].completed;
      if (completed && !completedTasksByUsers[userId]) {
        completedTasksByUsers[userId] = 0;
      }
      if (completed) ++completedTasksByUsers[userId];
    }
    console.log(completedTasksByUsers);
  }
});
