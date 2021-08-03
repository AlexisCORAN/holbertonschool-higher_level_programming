#!/usr/bin/node
const myArgs = process.argv.slice(2);
const value = parseInt(myArgs[0]);
if (isNaN(value)) {
  console.log('Missing size');
} else {
  const value = myArgs[0];
  for (let i = 0; i < value; i++) {
    console.log('X'.repeat(value));
  }
}
