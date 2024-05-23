#!/usr/bin/node
/**
 * Star Wars Characters
 */
const request = require('request');

const args = process.argv.slice(); // remove the first 2 args

const filmId = args.pop();
const url = 'https://swapi-api.alx-tools.com/api/films/' + filmId;

function fetchFilm (url) {
  return new Promise((resolve, reject) => {
    request(url, { json: true }, (err, response, body) => {
      if (err) {
        reject(new Error('Error fetching film'));
        return;
      }

      if (response.statusCode !== 200) {
        reject(new Error('Failed to fetch film'));
        return;
      }

      resolve(body);
    });
  });
}

async function fetchCharacters (filmBody) {
  const charactersUrls = filmBody.characters;
  if (charactersUrls === undefined) {
    return [];
  }

  const characters = [];
  for (const characterUrl of charactersUrls) {
    const body = await fetchCharacter(characterUrl);
    if (body.name !== undefined) {
      characters.push(body.name);
    }
  }

  return characters;
}

function fetchCharacter (characterUrl) {
  return new Promise((resolve, reject) => {
    request(characterUrl, { json: true }, (err, response, body) => {
      if (err) {
        reject(new Error(`Error fetching character from ${characterUrl}`));
        return;
      }

      if (response.statusCode !== 200) {
        reject(new Error(`Failed to fetch character from ${characterUrl}`));
        return;
      }

      resolve(body);
    });
  });
}

async function main () {
  try {
    const filmBody = await fetchFilm(url);
    const characters = await fetchCharacters(filmBody);

    for (const character of characters) {
      console.log(character);
    }
  } catch (error) {
    console.error(error);
  }
}

main();
