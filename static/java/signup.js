document.addEventListener("DOMContentLoaded", () => {
  const form = document.getElementById("signupForm");
  const spinner = document.querySelector(".loading-spinner");
  const check = document.querySelector(".success-check");
  const btnText = document.querySelector(".button-text");

  form.addEventListener("submit", (e) => {
    e.preventDefault(); // stop default page reload

    // Reset states in case the button was used before
    spinner.style.display = "block";
    check.style.display = "none";
    btnText.textContent = "Creating...";

    // Simulate AJAX request — replace with real API call
    setTimeout(() => {
      spinner.style.display = "none";
      check.style.display = "block";
      btnText.textContent = "Success!";
      
      // Optional: Reset form after success
      form.reset();
    }, 2000);
  });
});
