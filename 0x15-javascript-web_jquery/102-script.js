const apiUrl = 'https://www.fourtonfish.com/hellosalut/?lang=';

$('document').ready(function () {
  $('INPUT#btn_translate').click(() => {
    const lang = $('INPUT#language_code').val();
    $.get(apiUrl.concat(lang), (data) => {
      $('DIV#hello').text(data.hello);
    });
  });
});
