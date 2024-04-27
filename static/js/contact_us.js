// script.js
document.getElementById('contactForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent the form from submitting in the traditional way

    // Collecting form data
    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    const phone = document.getElementById('phone').value;
    const message = document.getElementById('message').value;

    // Ideally, here you would send this data to a server
    console.log("Contact Form Data:", { name, email, phone, message });
    alert("Thank you for contacting us, " + name + "! We will get back to you soon.");

    // Optionally reset the form
    event.target.reset();
});
