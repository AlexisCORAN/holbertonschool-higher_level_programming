#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const filePath = process.argv[3];

request(process.argv[2], function (err, response, body) {
  fs.writeFile(process.argv[3], body, 'utf8', function (err) {
    if (err) {
      console.log(err);
    }
  });
});
