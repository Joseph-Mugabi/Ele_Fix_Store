$(document).ready( function() {$('#action').click(
  function(event){
     /*var id = $("#pt").text();*/
     var id = window.location.pathname.split('/')[2];
     var route = `http://127.0.0.1:5001/api/v1/customers/${id}`;
   $.ajax(
	   {
		   url: route,
		   type: 'DELETE',
		   success: function(result){
			console.log('Deleted Successfully');
			window.location.href = `/`;
		   },
		   error: function(xhr, status, error ) {
			   console.log(error);
		           console.log(id);

		   }
	   }     
   );
  }
);});
