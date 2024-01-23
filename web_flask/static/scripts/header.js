class MyHeader extends HTMLElement {
    connectedCallback() {
      this.innerHTML = `
      <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" href="/styles/customers_store.css" />
        
      </head>
  
        <header class="head">
          <nav>
            <img
              src="https://assets.mockflow.com/app/wireframepro/company/C06cebf9edc514714a50cc24918f5b156/projects/MYQX0R3SPob/images/thumbnails/Me6d09e02eed3c78df2c2c0e04e0817c21678708408116"
              alt="photo"
              class="left-side-img3"
            />
            <h1><a class="title" href="/">Ele_Fix_Store</a></h1>
            <!-- Displayed navigation elements -->
            <ul class="displayed-nav">
                <li><a class="customers" href="/">Customers</a></li>
                <li><a class="store" href="/store">Store</a></li>
                <li><a class="appointments" href="/appointments">Appointments</a></li>
            </ul>

            

            <!-- Hidden navigation elements -->
            <ul id="hiddenNav" class="hidden-nav" >
                <li><a href="/procurements">Procurement</a></li>
                <li><a href="/services">Services</a></li>
                <li><a href="/AI">Chat AI</a></li>
                <li><a href="/chat">Discussion</a></li>
            </ul>
            </nav>

            <div id="buttonSection" class="button-section">
                <!-- Toggle button for hidden navigation elements -->
                <button class="navbar-toggler" onclick="toggleHiddenNav()">
                    <img src="/static/images/menu-icon.svg" id = "tog" alt="icon-menu"  />
                </button>
            </div>
  
          <div class="prof" id="homepage">
            <div style="text-align: center;">
              <img id="userPhoto" src="/static/images/person_FILL0_wght400_GRAD0_opsz48.png" alt="User Photo" class="user-photo" onclick="showProfile()" />
              <h1 class="customer-name">
                <script>
                    // Assign the user name to a JavaScript variable
                    var userName = "{{ user.name }}";
                    document.write(userName);
                </script>
              </h1>
            </div>
  
            <div id="profileSection" style="display: none;">
              <div class="profile">
                <div style="display: flex; margin-top: 10px;">
                    <img src="/static/images/home-icon.svg" alt="home" style="margin-top: -10px; width: 50px; height: 50px;" />
                    <h2><a href="/" style="text-decoration: none; font-size: 20px; margin-left: -15px; color: black; font-weight: lighter; ">Home<a></h2>
                </div>
               
                <div style="display: flex; margin-top: -25px;">
                    <img src="/static/images/person_FILL0_wght400_GRAD0_opsz48.png" alt="User Photo" class="user-photo" style="margin-top: -16px; width: 50px; height: 50px; margin-left: -3px;" />
                    <h2><a href="/" style="text-decoration: none; font-size: 20px; margin-left: -30px; color: black; font-weight: lighter; ">Profile<a></h2>
                </div>
                
                <div style="display: flex; margin-top: -35px;">
                    <img src="/static/images/logout-icon.svg" style="margin-top: -10px; width: 40px; height: 40px;" />
                    <h3 class="button1" id="logoutButton" style="margin-top: px; margin-left: -20px; font-weight: lighter;"><a href="http://127.0.0.1:5000/logout" style="text-decoration: none; margin-left: -20px; font-size: 20px;">Logout</a></h3>
                </div>
              </div>
            </div>
          </div>
        </header>
      `;
  
      // Create a style element for the CSS styles
      const styleElement = document.createElement('style');
      styleElement.textContent = `
        /* CSS styles */
          * {
          padding: 5px;
          margin: 0;
          box-sizing: border-box;
          font-size: 14px;
          
        }
        .head {
          background-color: hsl(140, 84%, 42%);
          position: fixed;
          z-index: 100;
          top: 0;
          left: 0;
          right: 0;
          height: 10%;
          align-items: flex-start;
          display: flex;
          box-shadow: 2px 2px 10px #9c9a9a;
        }
  
        ul {
          list-style: none; /* Removes bullet points */
        }
  
        li {
          display: inline-block; /* Displays list items inline */
          margin-right: 10px; /* Adds a small space between each item */
        }
  
        .left-side-img3 {
          height: 38px;
          width: 80px;
          left: 0%;
          align-items: center;
        }
  
        .title {
          height: 50%;
          width: 50%;
          top: 5px;
          position: absolute;
          display: flex;
          flex-direction: column;
          justify-content: space-around;
          padding: 2rem;
          left: 5.5%;
          font-size: 27px;
          color: rgb(240, 248, 255);
          font-family: 'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif;
          text-decoration: none;
        }

        .button-section {
            display: flex;
            justify-content: space-around;
            back-ground: hsl(140, 84%, 42%);
            top: -13%;
            align-items: center;
            position: relative;
            margin-left: 70%;
            
          }
          
          .navbar-toggler {
            justify-content: space-around;
            height: fit-content;
            background: none;
            border: none;
            z-index: 3;
            cursor: pointer;
          }
          
          .hidden-nav {
            display: none;
            position: absolute;
            top: 100%; 
            left: 25%;
            width: 100%; 
            text-decoration: none;
          }

          .show {
            display: block;
            background-color: hsl(140, 84%, 42%);
            width: fit-content;
            margin-left: 50%;
        }

          .hidden-nav a{
            text-decoration: none;
            color: white;
            font-size: 19px;
            font-weight: bold;
            font-family: 'Arial Narrow', Arial, sans-serif;
          }
        
        .hidden-nav.show {
            display: block;
            display: flex;
            flex-direction: column;
            align-items: center;
            text-decoration: none;
        }
  
        .customers {
          height: 15%;
          width: 10%;
          top: 23%;
          left: 30%;
          position: absolute;
          display: flex;
          flex-direction: column;
          justify-content: space-around;
          padding: 1rem;
          color: rgb(245, 248, 250);
          text-decoration: none;
          font-size: 19px;
          font-weight: bold;
          font-family: 'Arial Narrow', Arial, sans-serif;
        }
  
        .store {
          height: 15%;
          width: 10%;
          top: 23%;
          left: 45%;
          position: absolute;
          display: flex;
          flex-direction: column;
          justify-content: space-around;
          padding: 1rem;
          color: rgb(245, 248, 250);
          text-decoration: none;
          font-size: 18px;
          font-weight: bold;
          font-family: 'Arial Narrow', Arial, sans-serif;
        }
  
        .appointments {
          height: 15%;
          width: 10%;
          top: 23%;
          left: 60%;
          position: absolute;
          display: flex;
          flex-direction: column;
          justify-content: space-around;
          padding: 1rem;
          color: rgb(245, 248, 250);
          text-decoration: none;
          font-size: 18px;
          font-weight: bold;
          font-family: 'Arial Narrow', Arial, sans-serif;
        }
  
        /* Styling for the user profile section */
        .prof {
          top: -17%;
          left: -10%;
          position: absolute;
          display: flex;
          flex-direction: column;
          justify-content: space-around;
          padding: 1rem;
          float: right;
          margin-left: 99%;
        }
  
        .profile {
          width: fit-content;
          height: fit-content;
          border-radius: 50%;
          margin-left: -20px;
          margin-top: 0px;
          position: absolute;
          padding: 0px;
          border: 1px solid hsl(140, 84%, 42%, 0.8);
          background-color: white;
          border-radius: 5px;
        }

        .profile.div {
            display: flex;
            align-items: inline-flex;
        }
  
        
  
        .profile label {
          display: block;
          margin-bottom: 2px;
          text-align: center;
          font-weight: bold;
          font-size: 20px;
        }
  
        .profile input[type="text"] {
          width: 100%;
          padding: 5px;
          margin-bottom: 5px;
          border-radius: 5px;
        }
  
        .profile span {
          display: block;
          margin-bottom: 10px;
          text-align: center;
          font-size: 20px;
        }
  
        .profile button {
          display: block;
          width: 100%;
          padding: 10px;
          margin-top: 10px;
        }
  
        /* Styling for the user photo */
        .user-photo {
          cursor: pointer;
          width: 45px;
          height: auto;
        }
  
        /* Styling for the edit mode */
        .edit-mode .profile span {
          display: none;
        }
  
        .edit-mode .profile input[type="text"] {
          display: block;
          background-color: #f5f5f5;
        }
  
        .edit-mode .profile .edit-buttons {
          display: block;
        }
  
        .edit-mode .profile .edit-buttons button {
          display: inline-block;
          margin-right: 10px;
        }
  
        .button1 {
          background-color: #20b140;
          border-radius: 5px;
          color: white;
          padding: 8px 20px;
          border: none;
          background-color: hsl(120, 64%, 35%);
          font-family: "Montserrat", sans-serif;
          font-weight: 200;
        }
  
        .button1 {
          margin-left: -20px;
          background: none;
          border-radius: 5px;
          padding: 8px 20px;
          border: none;
          font-family: "Montserrat", sans-serif;
          font-weight: 200;
          margin-top: -10px;
        }

        .button1 a {
          font-size: 25px;
          color: red;
          margin-top: -10px;
        }
  
        .button1:hover {
          background-color: hsl(180, 7%, 97%);
          color: rgb(5, 121, 5);
          border: 2px ;
        }
  
        .button1:hover {
          background: none;
          color: rgb(240, 10, 10);
          border: none;
        }
  
        /* Media query for small screens */
        @media only screen and (max-width: 767px) {
          .title {
            font-size: 20px;
          }
  
          .left-side-img3 {
            width: 50px;
            height: 30px;
          }
  
          .customers,
          .store,
          .appointments {
            margin-left: -30px;
          }
  
          .user-photo {
            width: 30px;
            height: 30px;
          }
        }
  
        /* Media query for extra small screens */
        @media only screen and (max-width: 479px) {
          .left-side-img3 {
            height: 40px;
          }
  
          .title {
            font-size: 16px;
          }
  
          .user-photo {
            width: 24px;
            height: 24px;
          }
  
          .customers,
          .store,
          .appointments {
            font-size: 20px;
            margin-left: -30px;
          }
        }

        /* CSS styles for small screens */
        @media only screen and (max-width: 767px) {
            .displayed-nav,
            .hidden-nav {
                display: none;
            }

            .button-section {
                display: block;
            }
        }

        #tog{
          width: 45px;
          height; auto;
        }

        
      `;
  
      // Append the style element to the document's head section
      document.head.appendChild(styleElement);
  
      // Create a script element
      const scriptElement = document.createElement('script');
  
      // Set the script content directly
      scriptElement.textContent = `
        // JavaScript code here
        console.log('Script executed!');

        function toggleHiddenNav() {
          var hiddenNav = document.getElementById('hiddenNav');
          hiddenNav.classList.toggle('show');
      }
  
      // Show/hide hidden navigation on toggle button click
      function showHiddenNavOnToggle() {
          var hiddenNav = document.getElementById('hiddenNav');
          var toggleButton = document.querySelector('.navbar-toggler');
  
          toggleButton.addEventListener('click', function() {
              hiddenNav.classList.toggle('show');
          });
      }
  
      // Call the function on page load
      window.addEventListener('click', showHiddenNavOnToggle);
  
      
      // Function to display the user profile
      function showProfile() {
        var profileSection = document.getElementById("profileSection");
        profileSection.style.display = "block";
        
        // Add event listener to the document to handle clicks outside the profile section
        document.addEventListener("click", handleClickOutsideProfile);
      }
      
      // Function to handle clicks outside the profile section
      function handleClickOutsideProfile(event) {
        var profileSection = document.getElementById("profileSection");
        var userPhoto = document.getElementById("userPhoto");
        
        // Check if the clicked element is outside the profile section and user photo
        if (!profileSection.contains(event.target) && !userPhoto.contains(event.target)) {
          profileSection.style.display = "none";
          
          // Remove the event listener after hiding the profile section
          document.removeEventListener("click", handleClickOutsideProfile);
        }
      }
      
       
      `;
  
      // Append the script element to the document's head or body section
      document.head.appendChild(scriptElement);
      // or document.body.appendChild(scriptElement);
    }
  }
  
  customElements.define("my-header", MyHeader);
  
