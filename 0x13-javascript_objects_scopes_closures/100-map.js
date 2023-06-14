#!/usr/bin/node
const list = require('./100-data.js').list;
const multIndex = (num, index) => {
  return num * index;
};

const newList = list.map(multIndex);
console.log(list);
console.log(newList);
