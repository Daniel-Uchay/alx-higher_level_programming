const movieId = process.argv[2];
const url = `https://swapi.dev/api/films/${movieId}/`;

fetch(url)
  .then(response => {
    if (!response.ok) {
      throw new Error(`Failed to retrieve movie data for ID ${movieId}`);
    }
    return response.json();
  })
  .then(movieData => {
    const characters = movieData.characters;
    for (const characterUrl of characters) {
      fetch(characterUrl)
        .then(response => {
          if (!response.ok) {
            throw new Error(`Failed to retrieve character data for URL ${characterUrl}`);
          }
          return response.json();
        })
        .then(characterData => {
          console.log(characterData.name);
        })
        .catch(error => {
          console.error(error.message);
        });
    }
  })
  .catch(error => {
    console.error(error.message);
  });
