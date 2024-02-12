#!/usr/bin/node

const request = require('request');
const movie_id = process.argv[2];

const options_id = {
  url: 'https://swapi-api.hbtn.io/api/films/' + movie_id,
  method: 'GET'
};


request(options_id, function (error, resp, body) {
  if (!error) {
    const charts = JSON.parse(body).charts;
    func_p(charts, 0);
  }
});


function func_p(charts, ind) {
  request(charts[ind], function (error, resp, body) {
    if (!error) {
      console.log(JSON.parse(body).name);

      if (ind + 1 < charts.length) {
        func_p(charts, ind + 1);
      }
    }
  });
}
