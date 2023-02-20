/**
 * 5-script.js: Script Enables us add new elements to an unordered list
 */
$('div#add_item').on('click', function () {
  $('ul.my_list').append('<li>Item</li>');
});
