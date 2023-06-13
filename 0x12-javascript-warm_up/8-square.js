#!/usr/bin/node
const args = process.argv;
const value = parseInt(args[2]);
if (isNaN(value)) {
  console.log('Missing size');
} else {
  let i;
  for (i = 0; i < value; i++) {
    console.log('X'.repeat(value));
  }
}
