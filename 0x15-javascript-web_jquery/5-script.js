// Dynamically appends a new list item when a div is clicked.
$(function () {
  $('div#add_item').on('click', function () {
    $('ul.my_list').append('<li>Item</li>');
  });
});
