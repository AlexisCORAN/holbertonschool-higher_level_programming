#!/usr/bin/node
const myArgs = process.argv.slice(2);
if (myArgs.length === 1) {
  myArgs.forEach((val) => {
    console.log(`${val}`);
  });
} else {
  console.log('No argument');
}
