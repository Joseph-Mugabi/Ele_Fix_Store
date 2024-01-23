$(document).ready(
  function() {
    $('#submitBtn').click(
	function(event){
         event.preventDefault();
	 $('#myform').submit();
	}
    )
    $('#sub_customer').submit(
	function(event) {
          event.preventDefault();
	  var form_data = $(this).serializeArray();
	  var json_data = {};
	  $.each(form_data, function (index, obj){
            json_data[obj.name] = obj.value;
	  });
	  $.ajax({
            type: 'POST',
	    url: 'http://127.0.0.1:5001/api/v1/customers',
	    data: JSON.stringify(json_data),
	    contentType: 'application/json',
	    success: function(data){
               console.log('Success!', data);
	    },
	    error: function(jqXHR, textStatus, errorThrown){
	       console.log('Error!', textStatus, errorThrown);
	  }
	  });
	});
  });
