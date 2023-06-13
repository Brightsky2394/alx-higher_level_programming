#!/usr/bin/node
const args = process.argv;
function factorial (m) {
  return (m === 0 || isNaN(m) ? 1 : m * factorial(m - 1));
}
console.log(factorial(Number(args[2])));
