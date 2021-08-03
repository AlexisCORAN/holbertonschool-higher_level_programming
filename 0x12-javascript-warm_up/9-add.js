#!/usr/bin/node
const myArgs = process.argv.slice(2);
function add (a, b) {
  return (a + b);
}

const a = parseInt(myArgs[0]);
const b = parseInt(myArgs[1]);

console.log(add(a, b));
