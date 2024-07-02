
    document.addEventListener('DOMContentLoaded', function() {
    const searchInput = document.getElementById('search');
    searchInput.addEventListener('input', function() {
        const searchValue = searchInput.value.trim();
        if (searchValue) {
            console.log(`Searching for: ${searchValue}`);
        }
    });
});