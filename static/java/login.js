document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("loginForm");
    const spinner = document.querySelector(".loading-spinner");
    const check = document.querySelector(".success-check");
    const btnText = document.querySelector(".button-text");

    form.addEventListener("submit", (e) => {
        spinner.style.display = "block";
        btnText.textContent = "Signing in...";
    });

    // Small animation for successful login (can be triggered if needed)
    form.addEventListener("ajax:success", () => {
        spinner.style.display = "none";
        check.style.display = "block";
        btnText.textContent = "Success!";
    });
});
