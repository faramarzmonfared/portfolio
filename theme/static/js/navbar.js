/**
 * Mobile navigation menu toggle behavior.
 */

function setupMobileMenu() {
    const button = document.getElementById("mobile-menu-toggle");
    const menu = document.getElementById("mobile-menu");
    if (!button || !menu) {
        return;
    }
    button.addEventListener("click", function () {
        menu.classList.toggle("hidden");
    });
}

document.addEventListener("DOMContentLoaded", setupMobileMenu);
