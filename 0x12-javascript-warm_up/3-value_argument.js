#!/usr/bin/node
const myArgs = process.argv.slice(2);
if (typeof myArgs[0] === 'undefined') {
  console.log('No argument');
}
myArgs.forEach((val) => {
    console.log(`${val}`);
});
