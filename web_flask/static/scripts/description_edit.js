const save = document.getElementById("save")
const items = document.getElementById("items");
const formData = new FormData();
var table = document.getElementById('table');
var item_Id;
item_Id = items.value;
formData.append("item_id", item_Id);

items.addEventListener("change", function() {
    item_Id = items.value;    
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

    var newRow = table.insertRow(1); // Insert new row below the table header (index 1)

    // Create new cells and set their content
    var cell1 = newRow.insertCell(0);
    cell1.textContent = 'Dummy Store';

    var cell2 = newRow.insertCell(1);
    cell2.textContent = '10 mg';

    var cell3 = newRow.insertCell(2);
    cell3.textContent = '3 times';

    var cell4 = newRow.insertCell(3);
    cell4.textContent = '7 days';

    var cell5 = newRow.insertCell(4);
    cell5.textContent = '2023-07-08';

    const url = `http://127.0.0.1:5001/api/v1/describe_item/${description_id}`;
    const data = {
        method: "POST",
        body: formData,
    }

    fetch(url, data).then(
        (response) => response.json()
    ).then(
        (data) => {console.log(data);
            
        }
        
    ).catch(
        (error) => {console.log(error);}
    );

});
