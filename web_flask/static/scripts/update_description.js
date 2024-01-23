const items = document.getElementById("items");
const formData = new FormData();
var item_Id;
item_Id = items.value;
console.log(item_Id);
formData.append("item_id", item_Id);
var item_name = items.options[items.selectedIndex].textContent;

items.addEventListener("change", function() {
    item_Id = items.value;
    const selectedIndex = items.selectedIndex;
    item_name = items.options[selectedIndex].textContent;  
    console.log(item_Id);
    formData.delete("item_id");
    formData.append("item_id", item_Id);
});

//edit described_item
btn.addEventListener("click", (event) => {
    event.preventDefault();
    const advise = document.getElementById("advise").value;
    const customer_id = window.location.pathname.split('/')[4];
    const description_id = window.location.pathname.split('/')[3];
    const described_item_id = window.location.pathname.split('/')[2];

    formData.append("advise", advise);
    formData.append("item_id", item_Id);
    
    const url = `http://127.0.0.1:5001/api/v1/described_item/${described_item_id}`
    const data = {
        method: "PUT",
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
        window.location.href=`/descriptions_edit/${description_id}/${customer_id}`
    })
    .catch((error) => {
        console.log(error);
    });

});
