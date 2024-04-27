document.getElementById('feedbackForm').addEventListener('submit', function(event) {
    event.preventDefault();

    var formData = {
        name: document.getElementById('name').value,
        email: document.getElementById('email').value,
        comments: document.getElementById('comments').value
    };

    console.log('Feedback Received:', formData);
    alert('Thank you for your feedback.');
});

const starRating = document.querySelector('.star-rating');
starRating.addEventListener('change', function(e) {
    console.log("Selected Rating: " + e.target.value);
});
