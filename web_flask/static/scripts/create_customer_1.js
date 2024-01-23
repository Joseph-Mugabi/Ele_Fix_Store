$('#sub_customer').click(
	function(event) {
		var name = $('#name').val();
		var gender = $('gender').val()

		$.post("http://127.0.0.1:5001/api/v1/customers", {
			'name': name,
			'gender': gender
		}, function (response) {
			console.log(response.message);
		});
	}
);
