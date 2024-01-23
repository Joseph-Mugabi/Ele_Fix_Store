const previousButton = document.getElementById('previousButton');
  const nextButton = document.getElementById('nextButton');
  const testimonialsContainer = document.querySelector('.testimonials-section .container');
  const testimonialItems = document.querySelectorAll('.testimonials-section li');
  const itemsPerPage = {
    lg: 3, // Number of items per page on large screens
    md: 3,
    sm:2  // Number of items per page on medium screens
  };
  let currentPage = 1;

  function updatePaginationButtons() {
    previousButton.style.display = currentPage > 1 ? 'block' : 'none';
  }

  function showTestimonialsForCurrentPage() {
    const startIndex = (currentPage - 1) * itemsPerPage.lg;
    const endIndex = startIndex + itemsPerPage[window.getComputedStyle(testimonialsContainer).getPropertyValue('grid-template-columns') === 'repeat(auto-fit,minmax(19rem,1fr))' ? 'lg' : 'md'];

    testimonialItems.forEach((item, index) => {
      if (index >= startIndex && index < endIndex) {
        item.style.display = 'block';
      } else {
        item.style.display = 'none';
      }
    });
  }

  function showNextPage() {
    currentPage++;
    showTestimonialsForCurrentPage();
    updatePaginationButtons();
  }

  function showPreviousPage() {
    currentPage--;
    showTestimonialsForCurrentPage();
    updatePaginationButtons();
  }

  nextButton.addEventListener('click', showNextPage);
  previousButton.addEventListener('click', showPreviousPage);

  showTestimonialsForCurrentPage();
  updatePaginationButtons();
