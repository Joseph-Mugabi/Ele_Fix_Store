//add item to customer
const names = document.querySelectorAll('.card');

names.forEach(name => {
    name.addEventListener('click', (event)=>{
        const customerId = window.location.pathname.split('/')[2];
        const itemId =  name.querySelector("#item_id").textContent
        const requestOptions = {
            method: 'POST',
        }

        console.log(customerId);
        console.log(itemId);

        fetch(`http://127.0.0.1:5001/api/v1/customer/${customerId}/item/${itemId}`, requestOptions).then(response => {
            if (response.ok) {
                return response.json();
            }
            throw new Error('Request failed!');
        }).then(data => {
            console.log(data);
            window.location.href = "/prescriptions/" + customerId;
        }).catch(error => { 
            console.log(error);
        });
    });
});
