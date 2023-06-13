#!/usr/bin/node
const args = process.argv;
const value = parseInt(args[2]);
if (isNaN(value))
{
	let res = "Not a number";
	console.log(res);
}
else
{
	let res1 = "My number: " + value;
	console.log(res1);
}
