const apiUrl = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';
$.get(apiUrl, function (actor) {
  $('DIV#character').text(actor.name);
});
