$('#myForm').submit(function(event) {
  event.preventDefault();

  var formData = {
    name: $('#name').val(),
    gender: $('#gender').val()
  };

  $.ajax({
    url: $(this).attr('action'),
    type: $(this).attr('method'),
    data: JSON.stringify(formData),
    contentType: 'application/json',
    success: function(response) {
      console.log(response);
    },
    error: function(error) {
      console.error(error);
    }
  });
});


