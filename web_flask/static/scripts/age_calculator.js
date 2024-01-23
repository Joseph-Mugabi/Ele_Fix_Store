// Get the date of birth input field
var dobField = document.getElementById('dob');

// Add an event listener to the date of birth field
dobField.addEventListener('blur', function() {
  // Get the value of the date of birth input field
  var dob = this.value;
  
  // Calculate the age and display it in the age input field
  var age = calculateAge(dob);
  document.getElementById('age').value = age;
});

// Function to calculate the age based on a date of birth
function calculateAge(dob) {
  var now = new Date();
  var dobDate = new Date(dob);
  var ageInMilliseconds = now - dobDate;
  var ageInYears = ageInMilliseconds / (1000 * 60 * 60 * 24 * 365.25);
  return Math.floor(ageInYears);
}
