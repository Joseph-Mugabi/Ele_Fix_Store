document.getElementById('sign_up').addEventListener('click', function(e) {
    e.preventDefault(); // Prevent default form submission behavior

    // Get form input values
    var email = document.getElementById('email1').value;
    var password = document.getElementById('password1').value;
    var name = document.getElementById('name1').value;
    var gender = document.getElementById('gender1').value;
    var location = document.getElementById('location1').value;
    var role = document.getElementById('role1').value;
    // Create an object with the form data
    var formData = new FormData();
    formData.append("email", email);
    formData.append("password", password);
    formData.append("name", name);
    formData.append("gender", gender);
    formData.append("location", location);
    formData.append("role", role);

    // Make a POST request to the API endpoint
    fetch('http://127.0.0.1:5000/signup', {
      method: 'POST',
      body: formData
    })
    .then(function(response) {
      if (response.ok) {
        // Successful login, redirect to home page
        window.location.href = "/";
      } else {
        // Failed login, display error message
        alert('Sign Up failed. Please check your credentials.');
      }
    })
    .catch(function(error) {
      console.error('Error:', error);
      alert('An error occurred during Sign Up.');
    });
  });
