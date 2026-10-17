// ==========================================
// SOLUTIONS: Event Listeners
// ==========================================

// --- Solution 1 ---
const toggleBtn = document.querySelector('#toggleBtn');

toggleBtn.addEventListener('click', (event) => {
    const currentColor = event.target.style.backgroundColor;
    event.target.style.backgroundColor = (currentColor === 'green') ? 'blue' : 'green';
});

// --- Solution 2 ---
const searchBox = document.querySelector('#searchBox');

searchBox.addEventListener('keyup', (event) => {
    if (event.key === 'Enter') {
        console.log(`Searching for: ${event.target.value}`);
    }
});