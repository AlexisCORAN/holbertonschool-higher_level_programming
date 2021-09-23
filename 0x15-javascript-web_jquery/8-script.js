const url = 'https://swapi-api.hbtn.io/api/films/?format=json';
$.get(url, function (data) {
  data.results.forEach((element) => {
    $('#list_movies').append('<li>' + element.tittle + '</li>');
  });
});
