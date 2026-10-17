// ==========================================
// 1. THE ADDEVENTLISTENER METHOD
// ==========================================

const button = document.querySelector('#myButton');

// Using a standard callback function
button.addEventListener('click', function() {
    console.log('Button was clicked!');
});

// Using an arrow function with the Event Object
button.addEventListener('click', (event) => {
    console.log('Clicked element ID:', event.target.id);
});

// ==========================================
// 2. COMMON EVENT TYPES
// ==========================================

const inputField = document.querySelector('#username');

// Input event
inputField.addEventListener('input', (event) => {
    console.log('Current input value:', event.target.value);
});

// Keyboard event
window.addEventListener('keydown', (event) => {
    if (event.key === 'Escape') {
        console.log('Escape key pressed!');
    }
});