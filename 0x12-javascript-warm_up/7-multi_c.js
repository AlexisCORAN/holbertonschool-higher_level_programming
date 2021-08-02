#!/usr/bin/node
const myArgs = process.argv.slice(2);
if (myArgs.length === 0) {
  console.log('Missing number of occurrences');
} else if (myArgs.length === 1) {
  const value = myArgs[0];
  for (let i = 0; i < value; i++) {
    console.log('C is fun');
  }
}
