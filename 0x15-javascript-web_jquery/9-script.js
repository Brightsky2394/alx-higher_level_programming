const apiUrl = 'https://fourtonfish.com/hellosalut/?lang=fr';
$.get(apiUrl, function (data) {
  $('DIV#hello').text(data.hello);
});
