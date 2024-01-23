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
console.log(id);

fetch(`http://127.0.0.1:5001/api/v1/services/${id}` , requestOptions).then(
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
