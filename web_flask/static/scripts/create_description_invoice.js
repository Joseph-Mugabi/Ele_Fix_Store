const send = document.getElementById("send");
var customer = window.location.pathname.split('/')[2];

send.addEventListener("click", () => {
    const description_id = document.getElementById("p_id").textContent;
    fetch(`http://127.0.0.1:5001/api/v1//description_invoice/${description_id}`, {
        method: "POST",
    }).then(
        (response) => response.json()
    ).then((data) => {
        console.table(data);
        window.location.href = '/invoices/' + customer;
        function showFlashMessage(message, duration) {
        const flashMessage = document.getElementById('flashMessage');
        
        // Create a new message element
        const messageElement = document.createElement('div');
        messageElement.textContent = message;
        
        // Append the message element to the flash message container
        flashMessage.appendChild(messageElement);
        
        // Set a timer to remove the message after the specified duration
        setTimeout(function() {
            flashMessage.removeChild(messageElement);
        }, duration);
        }
        
        // Example usage:
        showFlashMessage('Invoice Successfully Generated!', 3000); // Display success message for 3 seconds
    }).catch(
        (error) => {
            console.log(error);
        }
    )
});


//Delete description
document.addEventListener('DOMContentLoaded', function() {
    var actionButton = document.getElementById('action');
    actionButton.addEventListener('click', function(event) {
        var id = document.getElementById("p_id").textContent;
        var route = `http://127.0.0.1:5001/api/v1/description/${id}`;
        var customer_id = window.location.pathname.split('/')[2];
        
        fetch(route, {
            method: 'DELETE'
        })
        .then(function(response) {
            if (response.ok) {
                console.log('Deleted Successfully');
                window.location.href = '/descriptions/' + customer_id;
            } else {
                throw new Error('Error: ' + response.status);
            }
        })
        .catch(function(error) {
            console.log(error);
            console.log(id);
        });
    });
});
