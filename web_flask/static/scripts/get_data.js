$("sub_customer").click(
	function(event) {
		$.ajax({
    type: "DELETE",
    url: "http://127.0.0.1:5001/api/v1/customers/be7c8d29-d91b-4f2c-88c4-eba44691c0cb",
    success: function(response) {
        console.log("Success:", response);
    },
    error: function(xhr, status, error) {
        console.log("Error:", error);
    }
});
	}
);
