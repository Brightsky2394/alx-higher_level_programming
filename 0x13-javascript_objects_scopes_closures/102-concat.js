#!/usr/bin/node

const fs = require('fs');
let content = '';
const argv = process.argv;
content = content.concat(fs.readFileSync(argv[2]));
content = content.concat(fs.readFileSync(argv[3]));
fs.writeFileSync(argv[4], content);
