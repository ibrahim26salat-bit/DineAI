document.addEventListener("DOMContentLoaded", function () {
    console.log("Welcome to DineAI");

    const button = document.querySelector("button");

    if (button) {
        button.addEventListener("click", function () {
            alert("Finding the best restaurants for you...");
        });
    }
});
