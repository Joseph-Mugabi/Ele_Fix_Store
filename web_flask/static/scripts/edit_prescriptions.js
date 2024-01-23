const save = document.getElementById("save")
const items = document.getElementById("items");
const formData = new FormData();
var item_Id;
item_Id = items.value;
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

save.addEventListener("click", () => {
    const dose = document.getElementById("advise").value;
    const description_id = document.getElementById("p_id").textContent;
    console.log(description_id)

    formData.append("advise", advise);
    formData.append("description_id", description_id);
    
    const url = `http://127.0.0.1:5001/api/v1/describe_item/${description_id}`
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
        addRow(advise, item_name);
        resetForm();
    })
    .catch((error) => {
        console.log(error);
    });

});

function addRow(advise, item_name) {
    let table = document.getElementById("medicines");
    let row = table.insertRow(1); // Insert at the second position (index 1)
  
    // Create table cells
    let cell1 = row.insertCell(0);
    let cell3 = row.insertCell(1);
    let cell6 = row.insertCell(2);
    let cell8 = row.insertCell(3);
    let cell9 = row.insertCell(4);
  
    // Add data to cells
    cell1.textContent = item_name;
    cell3.textContent = advise + " quality/quantity";
    cell9.textContent = getCurrentTime();
  }

  document.addEventListener('click', function(event) {
    var target = event.target;
    if (!cardPopup.contains(target) && target !== addButton && target !== save) {
      cardPopup.classList.add('hidden');
    }
  });

  function getCurrentTime() {
    const currentTime = new Date();
    const utcTime = currentTime.toISOString().replace("T", " ").replace("Z", "");
    return utcTime;
}


/*function resetForm() {
    const form = document.getElementById('yourFormId');
    form.reset();
}*/

document.addEventListener('DOMContentLoaded', function() {
    var cardPopup1 = document.getElementById('cardPopup1');
    var medicinesTable = document.getElementById('medicines');
    const description_id = document.getElementById("p_id").textContent;
    const customer_id = window.location.pathname.split('/')[3];
    

    var rows = medicinesTable.getElementsByTagName('tr');
for (var i = 0; i < rows.length; i++) {
  const row = rows[i];
  row.addEventListener('dblclick', function(event) {
    const trans = row.children[0].textContent;
    window.location.href = "/edit_described_item_form/" + trans + "/" + description_id + "/" + customer_id;
  });
}
  });


function addRow(advise, item_name) {
    let table = document.getElementById("store");
    let row = table.insertRow(1); // Insert at the second position (index 1)
  
    // Create table cells
    let cell1 = row.insertCell(0);
    let cell3 = row.insertCell(1);
    let cell6 = row.insertCell(2);
    let cell8 = row.insertCell(3);
    let cell9 = row.insertCell(4);
  
    // Add data to cells
    cell1.textContent = item_name;
    cell3.textContent = advise + " quality/quantity";
    cell9.textContent = getCurrentTime();
  }

  document.addEventListener('click', function(event) {
    var target = event.target;
    if (!cardPopup.contains(target) && target !== addButton && target !== save) {
      cardPopup.classList.add('hidden');
    }
  });


  //Delete
  const deleteIcons = document.querySelectorAll('.delete-icon');

deleteIcons.forEach((icon) => {

//var trans = this.parentNode.parentNode.querySelector(".transaction");
icon.addEventListener('click', function(event){
const row = event.target.closest('tr');
var trans = row.children[0]
var id = trans.textContent;

const requestOptions = {
	method: "DELETE",
}

fetch('http://127.0.0.1:5001/api/v1/described_item/' + id, requestOptions).then(
response => response.json()).then(
data => { 
	console.log(data);
	deleteRow(icon);
}
).catch(error => console.error);
});
});

function deleteRow(button) {
  const row = button.parentNode.parentNode;
  row.remove();
}
