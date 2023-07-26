#!/usr/bin/node
const url = process.argv[2];
const request = require('request');
request.get(url,
  (err, res, body) => {
    if (err) { console.log(err); } else {
      const completedTasksByUsers = {};
      const rbody = JSON.parse(body);
      for (let i = 0; i < rbody.length; i++) {
        const userId = rbody[i].userId;
        const completed = rbody[i].completed;
        if (completed && !completedTasksByUsers[userId]) { completedTasksByUsers[userId] = 0; } if (completed) { completedTasksByUsers[userId] += 1; }
      }
      console.log(completedTasksByUsers);
    }
  });
