const form = document.getElementById('water-usage-form');
const output = document.getElementById('output');

form.addEventListener('submit', function(event) {
  event.preventDefault();

  const field = document.getElementById('field').value;
  const date = document.getElementById('date').value;
  const source = document.getElementById('source').value;
  const method = document.getElementById('method').value;
  const meterReading = parseFloat(document.getElementById('meter-reading').value);
  const duration = parseFloat(document.getElementById('duration').value);
  const crop = document.getElementById('crop').value;
  const weather = document.getElementById('weather').value;

  let totalWaterUsed = "";

  if (meterReading && !isNaN(meterReading)) {
    // Placeholder for actual water usage calculation based on meter data
    totalWaterUsed = calculateWaterUsage(meterReading);
  } else if (duration && !isNaN(duration)) {
    // Placeholder for water usage calculation based on duration
    totalWaterUsed = calculateWaterUsageByDuration(duration);
  } else {
    totalWaterUsed = "Please provide valid meter reading or estimated duration.";
  }

  // Display output
  output.innerHTML = `
    <p><strong>Field:</strong> ${field}</p>
    <p><strong>Date:</strong> ${date}</p>
    <p><strong>Water Source:</strong> ${source}</p>
    <p><strong>Irrigation Method:</strong> ${method}</p>
    <p>${meterReading ? `<strong>Meter Reading (liters):</strong> ${meterReading}` : ''}</p>
    <p>${duration ? `<strong>Estimated Duration (hours):</strong> ${duration}` : ''}</p>
    <p><strong>Crop Type:</strong> ${crop}</p>
    <p><strong>Weather Conditions:</strong> ${weather}</p>
    <p>${totalWaterUsed}</p>
  `;
});

function calculateWaterUsage(meterReading) {
  // Placeholder for actual water usage calculation based on meter data
  // Example: Assuming 1 liter per unit of meter reading
  const waterUsed = meterReading * 1; // Adjust this factor as per actual data
  return `**Total Water Used:** ${waterUsed.toFixed(2)} liters`;
}

function calculateWaterUsageByDuration(duration) {
  // Placeholder for water usage calculation based on duration
  // Example: Assuming 10 liters per hour of irrigation
  const waterUsed = duration * 10; // Adjust this factor as per actual data
  return `**Total Water Used:** ${waterUsed.toFixed(2)} liters`;
}
