function calculateBudget() {
    var inputCost = parseFloat(document.getElementById('input-cost').value);
    var expectedYield = parseFloat(document.getElementById('expected-yield').value);
    var marketPrice = parseFloat(document.getElementById('market-price').value);

    var totalCost = inputCost * expectedYield;
    var revenue = expectedYield * marketPrice;
    var profit = revenue - totalCost;

    var resultDiv = document.getElementById('result');
    resultDiv.innerHTML = "<h2>Results</h2>" +
                          "<p>Total Cost: $" + totalCost.toFixed(2) + "</p>" +
                          "<p>Revenue: $" + revenue.toFixed(2) + "</p>" +
                          "<p>Profit: $" + profit.toFixed(2) + "</p>";
}
