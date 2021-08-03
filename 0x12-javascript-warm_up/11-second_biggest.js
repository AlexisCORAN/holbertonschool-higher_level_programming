#!/usr/bin/node
const myArgs = process.argv.slice(2);

if (myArgs.length === 0 || myArgs.length === 1) {
  console.log('0');
} else {
  const secondbiggest = myArgs.sort(function (a, b) { return b - a; });
  console.log(secondbiggest[1]);
}
