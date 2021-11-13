#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/'.concat(process.argv[2]);

request(url, function (err, response, body) {
  const characters = JSON.parse(body).characters;
  if (err) {
    console.log(err);
  }

  for (let i = 0; i < characters.length; ++i) {
    request(characters[i], function (cErr, cResponse, cBody) {
      console.log(JSON.parse(cBody).name);
    });
  }
});
