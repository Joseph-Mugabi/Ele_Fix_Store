document.getElementById('signin').addEventListener('click', function(e) {
    e.preventDefault(); // Prevent default form submission behavior

    // Get form input values
    var email = document.getElementById('email2').value;
    var password = document.getElementById('password2').value;

    // Create an object with the form data
    var formData = new FormData();
    formData.append("email", email);
    formData.append("password", password);

    // Make a POST request to the API endpoint
    fetch('http://127.0.0.1:5000/login', {
      method: 'POST',
      body: formData
    }).then(function(response) {
      if (response.ok) {
        // Successful login, redirect to home page
        window.location.href = "/";
      } else {
        // Failed login, display error message
        alert('Log in failed. Please check your credentials.');
      }
    })
    .catch(function(error) {
      console.error('Error:', error);
      alert('An error occurred during login.');
    });
  });
