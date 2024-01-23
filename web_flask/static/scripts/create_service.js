const submitButton = document.getElementById('btns');
submitButton.addEventListener('click', (event) => {
    event.preventDefault();
    const form = document.getElementById('myFormS');
    const formData = new FormData(form);

	const data = {};
  		for (const [key, value] of formData.entries()) {
    	data[key] = value;
 	 }

    const requestOptions = {
        method: 'POST',
        body: JSON.stringify(data),
	headers: {'Content-Type': 'application/json'}
    };
	

    fetch('http://127.0.0.1:5001/api/v1/services', requestOptions)
        .then(response => response.json())
        .then(data => {
			console.log(data);
			const id = data.id;
			window.location.href = '/services'
		})
        .catch(error => console.error(error));
});
