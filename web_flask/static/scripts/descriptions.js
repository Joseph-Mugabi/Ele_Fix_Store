document.addEventListener('DOMContentLoaded', function() {
  var addButton = document.getElementById('addButton');
  var cardPopup = document.getElementById('cardPopup');

  addButton.addEventListener('click', function(event) {
    event.preventDefault();
    cardPopup.classList.remove('hidden');
  });

  /*document.addEventListener('click', function(event) {
    var target = event.target;
    if (!cardPopup.contains(target) && target !== addButton) {
      cardPopup.classList.add('hidden');
    }
  });*/
});