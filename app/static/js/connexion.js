document.addEventListener('DOMContentLoaded', () => {
    document.querySelector('.form').addEventListener('submit', function (e) {
        e.preventDefault();
        localStorage.setItem('connected', 'true');
        window.location.href = '/';
    });
});