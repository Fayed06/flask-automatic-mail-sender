document.addEventListener("DOMContentLoaded", function() {
    const form = document.getElementById("emailForm");
    const responseMessage = document.getElementById("responseMessage");

    form.addEventListener("submit", function(event) {
        event.preventDefault();
        const formData = new FormData(form);
        
        fetch("/save_emails", {
            method: "POST",
            body: formData
        })
        .then(response => {
            if (response.ok) {
                return response.text();
            }
            throw new Error("Network response was not ok.");
        })
        .then(data => {
            responseMessage.textContent = "Email sent successfully!";
            form.reset();
        })
        .catch(error => {
            responseMessage.textContent = "Error sending email. Please try again.";
            console.error("Error sending email:", error);
        });
    });
});
