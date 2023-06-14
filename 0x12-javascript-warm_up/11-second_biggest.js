#!/usr/bin/node
const args = process.argv;
const arr = [];
let j = 0;
while (j < args.length) {
  arr[j] = Math.floor(Number(args[j + 2]));
  j++;
}
const filtered = arr.filter(n => !isNaN(n));
const sorted = filtered.sort(function (a, b) {
  return (a - b);
});
if (sorted.length < 2) {
  console.log(0);
} else {
  console.log(sorted[sorted.length - 2]);
}
