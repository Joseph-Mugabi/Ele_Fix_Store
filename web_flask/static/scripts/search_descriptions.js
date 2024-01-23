const searchQuery = document.getElementById('search-query');
const patient_id = window.location.pathname.split("/")[2]

searchQuery.addEventListener('keydown', (event) => {
  if (event.keyCode === 13) { // Enter key pressed
    event.preventDefault(); // prevent default form submission

    // Get the search query
    const query = searchQuery.value;

    // Construct the search URL
    const url = `http://127.0.0.1:5000/search_description/${patient_id}?q=${encodeURIComponent(query)}`;

    // Redirect to the search URL
    window.location.href = url;
  }
});
