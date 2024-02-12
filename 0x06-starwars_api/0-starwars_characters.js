#!/usr/bin/node

const request = require('request');
const mov = process.argv[2];

const optn = {
  url: 'https://swapi-api.hbtn.io/api/films/' + mov,
  method: 'GET'
};

request(optn, function (error, resp, body) {
  if (!error) {
    const charts = JSON.parse(body).characters;
    funcPrint(charts, 0);
  }
});

function funcPrint (charts, ind) {
  request(charts[ind], function (error, resp, body) {
    if (!error) {
      console.log(JSON.parse(body).name);

      if (ind + 1 < charts.length) {
        funcPrint(charts, ind + 1);
      }
    }
  });
}
