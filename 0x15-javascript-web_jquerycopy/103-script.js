// jQuery that fetches and replaces the name of this URL: 
// https://www.fourtonfish.com/hellosalut/?lang=fr

$('document').ready(function () {
  $('INPUT#btn_translate').click(translate);
  $('INPUT#language_code').focus(function () {
    $(this).keydown(function (ev) {
      if (ev.keyCode === 13) {
        translate();
      }
    });
  });
});

function translate () {
  const url = 'https://www.fourtonfish.com/hellosalut/?';
  $.get(url + $.param({ lang: $('INPUT#language_code').val() }), function (data) {
    $('DIV#hello').html(data.hello);
  });
}
