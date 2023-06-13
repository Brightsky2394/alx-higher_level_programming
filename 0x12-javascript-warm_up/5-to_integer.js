#!/usr/bin/node
const args = process.argv;
const value = parseInt(args[2]);
if (isNaN(value)) {
  const res = 'Not a number';
  console.log(res);
} else {
  const res1 = 'My number: ' + value;
  console.log(res1);
}
