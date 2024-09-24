#!/usr/bin/node
// This script prints all characters of a Star Wars movie based on
// its MOVIE ID.
// one character name per line in the same order as the
// “characters” list in the /films/ endpoint

const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

function getMovieStar (starUrl) {
  return new Promise(function (resolve, reject) {
    request(starUrl, function (error, response, body) {
      if (error) {
        reject(error);
      } else {
        resolve(JSON.parse(body).name);
      }
    });
  });
}

request(url, async function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const characters = JSON.parse(body).characters;
    for (const starUrl of characters) {
      console.log(await getMovieStar(starUrl));
    }
  }
}
);
