function calculateBalance() {
    var amount = parseFloat(document.getElementById("amount").value);
    var paid = parseFloat(document.getElementById("paid").value);
    var balance = amount - paid;
    document.getElementById("balance").value = balance.toFixed(2);
  }
