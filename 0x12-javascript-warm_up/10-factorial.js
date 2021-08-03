#!/usr/bin/node
const myArgs = process.argv.slice(2);

function factorial (num) {
  if (num === 0 || isNaN(num)) {
    return (1);
  }
  return (num * factorial(num - 1));
}

const num = parseInt(myArgs[0]);
console.log(factorial(num));
