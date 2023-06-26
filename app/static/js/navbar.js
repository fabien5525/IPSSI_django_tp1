document.addEventListener('DOMContentLoaded', () => {
    if (localStorage.getItem('connected') === 'true') {
        document.querySelector('.connection').style.display = 'none';
    }
});
