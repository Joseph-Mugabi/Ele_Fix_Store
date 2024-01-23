const services = document.getElementById("services");
const formData = new FormData();
var service_Id;
service_Id = services.value;
console.log(service_Id);
formData.append("service_id", service_Id);
var service_name = services.options[services.selectedIndex].textContent;

services.addEventListener("change", function() {
    service_Id = services.value;
    const selectedIndex = services.selectedIndex;
    service_name = services.options[selectedIndex].textContent;  
    console.log(service_Id);
    formData.delete("service_id");
    formData.append("service_id", service_Id);
});

//edit described_item
btn.addEventListener("click", (event) => {
    event.preventDefault();
    const invoice_id = window.location.pathname.split('/')[2];

    formData.append("service_id", service_Id);
    formData.append("invoice_id", invoice_id);
    
    const url = `http://127.0.0.1:5001/api/v1/invoice_services`
    const data = {
        method: "POST",
        body: formData,
    }

    fetch(url, data).then((response) => {
        if (response.ok) {
            return response.json();
        } else {
            throw new Error('Error: ' + response.status);
        }
    })
    .then((data) => {
        console.log(data);
        window.location.href=`/single_invoice/${invoice_id}`
    })
    .catch((error) => {
        console.log(error);
    });

});
