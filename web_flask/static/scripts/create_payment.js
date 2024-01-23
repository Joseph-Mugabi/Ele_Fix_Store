const submitButton = document.getElementById('btn');
submitButton.addEventListener('click', (event) => {
    event.preventDefault();
    const form = document.getElementById('myForm');
    const formData = new FormData(form);
    const customer_id = window.location.pathname.split('/')[2]
    const invoice_id = window.location.pathname.split('/')[3]

        const data = {};
                for (const [key, value] of formData.entries()) {
        data[key] = value;
         }

    const requestOptions = {
        method: 'POST',
        body: JSON.stringify(data),
        headers: {'Content-Type': 'application/json'}
    };

   


    fetch('http://127.0.0.1:5001/api/v1/payments/' + customer_id + "/" + invoice_id, requestOptions)
        .then(response => response.json())
        .then(data => {
                        console.log(data);
                        const my_id = data.id;
                       window.location.href = `/invoices/${id}`;
                })
        .catch(error => console.error(error));
});
