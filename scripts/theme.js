function toggleDarkMode() {
    document.body.classList.toggle('dark-mode');
    const isDark = document.body.classList.contains('dark-mode');
    localStorage.setItem('theme', isDark ? 'dark' : 'light');
    const toggle = document.getElementById('theme-toggle');
    if (toggle) toggle.textContent = isDark ? '☀️' : '🌙';
}

function initTheme() {
    const savedTheme = localStorage.getItem('theme');
    if (savedTheme === 'dark') {
        document.body.classList.add('dark-mode');
    } else if (!savedTheme && window.matchMedia('(prefers-color-scheme: dark)').matches) {
        document.body.classList.add('dark-mode');
        localStorage.setItem('theme', 'dark');
    }
    const toggle = document.getElementById('theme-toggle');
    if (toggle) {
        const isDark = document.body.classList.contains('dark-mode');
        toggle.textContent = isDark ? '☀️' : '🌙';
    }
}

if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initTheme);
} else {
    initTheme();
}
