#!/usr/bin/node
var myArgs = process.argv.slice(2);

if (myArgs.length === 2) {
  let first_value = myArgs[0];
  let second_value = myArgs[1];
  console.log('%s is %s', first_value, second_value);
}
