function toggleDarkMode() {
    document.body.classList.toggle('dark-mode');
    const isDark = document.body.classList.contains('dark-mode');
    localStorage.setItem('theme', isDark ? 'dark' : 'light');
    console.log('Theme toggled:', isDark ? 'dark' : 'light');
}

function initTheme() {
    const savedTheme = localStorage.getItem('theme');
    // Default to dark if no preference, or respect saved
    // Actually, user's current is light. Let's default to saved or light.
    if (savedTheme === 'dark') {
        document.body.classList.add('dark-mode');
    }
}

// Run on load
initTheme();
// Also attempt to run immediately in case of re-renders
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initTheme);
} else {
    initTheme();
}
