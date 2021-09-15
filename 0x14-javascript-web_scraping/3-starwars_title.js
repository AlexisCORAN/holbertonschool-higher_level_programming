#!/usr/bin/node

const request = require('request');
const StarWarsURL = 'https://swapi-api.hbtn.io/api/films/'.concat(process.argv[2]);

request(StarWarsURL, title);

function title (_err, _res, body) {
  body = JSON.parse(body);
  console.log(body.title);
}
