$(document).ready(function () {
  // Register submit handler
  $("#registration-form").submit(function (event) {
    // Prevent the default form submission
    event.preventDefault();

    // Get the form data
    var formData = {
      email: $("#email").val(),
      password: $("#password").val(),
      verify_password: $("#verify_password").val(),
    };

    // Send the data to the backend API using AJAX
    $.ajax({
      type: "POST",
      url: "/api/register",
      data: JSON.stringify(formData),
      contentType: "application/json",
      success: function (response) {
        // Handle the successful response from the backend API
        console.log(response);
        // Redirect to a success page or perform any other actions
      },
      error: function (xhr, status, error) {
        // Handle the error response from the backend API
        console.log(xhr.responseText);
        // Display an error message or perform any other error handling
      },
    });
  });
});
