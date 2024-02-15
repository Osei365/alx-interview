#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/';
const id = process.argv[2];

function logChars (array, i) {
  if (i === array.length) {
    return;
  }
  request.get(array[i], function (err1, response1, body1) {
    if (!err1) {
      console.log(JSON.parse(body1).name);
      logChars(array, i + 1);
    }
  });
}

request.get(url + id, function (err, response, body) {
  if (!err) {
    const chs = JSON.parse(body).characters;
    logChars(chs, 0);
  }
});
