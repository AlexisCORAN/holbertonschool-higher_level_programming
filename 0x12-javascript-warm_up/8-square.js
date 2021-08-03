#!/usr/bin/node
const myArgs = process.argv.slice(2);
if (myArgs.length === 0 || typeof myArgs[0] === 'string') {
  console.log('Missing size');
} else if (myArgs.length === 1) {
  const value = myArgs[0];
  for (let i = 0; i < value; i++) {
    console.log('X'.repeat(value));
  }
}
