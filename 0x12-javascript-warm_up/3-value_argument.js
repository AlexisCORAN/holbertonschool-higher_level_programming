#!/usr/bin/node
const myArgs = process.argv.slice(2);
if (myArgs  != 0) {
  myArgs.forEach((val) => {
    console.log(`${val}`);
  });
} else {
  console.log('No argument');
}
