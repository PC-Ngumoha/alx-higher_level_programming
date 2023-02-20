/**
 * 101-script.js: simple CRUD list using jquery
 */
$(function () {
  $('div#add_item').on('click', function () {
    $('ul.my_list').append('<li>Item</li>');
  });

  $('div#remove_item').on('click', function () {
    $('ul.my_list').children().last().detach();
  });

  $('div#clear_list').on('click', function () {
    $('ul.my_list').empty();
  });
});
