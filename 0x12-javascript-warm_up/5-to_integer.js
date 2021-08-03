#!/usr/bin/node
const myArgs = process.argv.slice(2);
const value = parseInt(myArgs[0]);

if (isNaN(value)) {
  console.log('Not a number');
} else {
  console.log('My number: %d', value);
}
