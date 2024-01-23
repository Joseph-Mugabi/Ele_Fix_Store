const addItemButton = document.getElementById('addItemButton');
const itemContainer = document.getElementById('itemContainer');
const submitButton = document.getElementById('submitButton');

addItemButton.addEventListener('click', () => {
    const itemRow = document.createElement('div');
    itemRow.className = 'item-row';

    const itemNameLabel = document.createElement('label');
    itemNameLabel.textContent = 'Item Name:';
    const itemNameInput = document.createElement('input');
    itemNameInput.type = 'text';
    itemNameInput.className = 'itemName';
    itemNameInput.name = 'itemName';
    itemNameInput.required = true;

    const quantityLabel = document.createElement('label');
    quantityLabel.textContent = 'Quantity:';
    const quantityInput = document.createElement('input');
    quantityInput.type = 'number';
    quantityInput.className = 'quantity';
    quantityInput.name = 'quantity';
    quantityInput.required = true;

    const priceLabel = document.createElement('label');
    priceLabel.textContent = 'Price:';
    const priceInput = document.createElement('input');
    priceInput.type = 'number';
    priceInput.className = 'price';
    priceInput.name = 'price';
    priceInput.required = true;

    itemRow.appendChild(itemNameLabel);
    itemRow.appendChild(itemNameInput);
    itemRow.appendChild(quantityLabel);
    itemRow.appendChild(quantityInput);
    itemRow.appendChild(priceLabel);
    itemRow.appendChild(priceInput);

    itemContainer.appendChild(itemRow);
});

submitButton.addEventListener('click', (event) => {
    event.preventDefault();

    const vendorName = document.getElementById('vendorName').value;

    const items = [];
    const itemRows = document.getElementsByClassName('item-row');
    for (let i = 0; i < itemRows.length; i++) {
        const itemName = itemRows[i].querySelector('.itemName').value;
        const quantity = itemRows[i].querySelector('.quantity').value;
        const price = itemRows[i].querySelector('.price').value;

        const item = {
            name: itemName,
            quantity: quantity,
            price: price
        };

        items.push(item);
    }

    const data = {
        vendor_name: vendorName,
        items: items
    };

    const requestOptions = {
        method: 'POST',
        body: JSON.stringify(data),
        headers: { 'Content-Type': 'application/json' }
    };

    fetch('http://127.0.0.1:5001/api/v1/procurements', requestOptions)
        .then(response => response.json())
        .then(data => {
            console.log(data);
            window.location.href = '/procurements';
        })
        .catch(error => console.error(error));
});
