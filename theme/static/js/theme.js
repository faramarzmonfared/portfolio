/**
 * Theme management: handles dark/light mode initialization and toggling.
 */

function getStoredTheme() {
    return localStorage.getItem("theme");
}

function prefersDarkScheme() {
    return window.matchMedia("(prefers-color-scheme: dark)").matches;
}

function applyTheme(isDark) {
    document.documentElement.classList.toggle("dark", isDark);
}

function initTheme() {
    const stored = getStoredTheme();
    const isDark = stored === "dark" || (!stored && prefersDarkScheme());
    applyTheme(isDark);
}

function syncToggleIcons(button) {
    const isDark = document.documentElement.classList.contains("dark");
    const iconLight = button.querySelector(".theme-icon-light");
    const iconDark = button.querySelector(".theme-icon-dark");
    iconLight.classList.toggle("hidden", isDark);
    iconDark.classList.toggle("hidden", !isDark);
}

function setupThemeToggle() {
    const button = document.getElementById("theme-toggle");
    if (!button) {
        return;
    }
    button.addEventListener("click", function () {
        const isDark = document.documentElement.classList.toggle("dark");
        localStorage.setItem("theme", isDark ? "dark" : "light");
        syncToggleIcons(button);
    });
    syncToggleIcons(button);
}

initTheme();
document.addEventListener("DOMContentLoaded", setupThemeToggle);