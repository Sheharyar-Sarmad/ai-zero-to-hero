// ==========================================
// SOLUTIONS: LocalStorage & JSON
// ==========================================

const usernameInput = document.querySelector('#usernameInput');
const saveBtn = document.querySelector('#saveBtn');
const displayDiv = document.querySelector('#displayDiv');

// --- Solution 1: Saving a Simple String ---
saveBtn.addEventListener('click', () => {
    const name = usernameInput.value.trim();
    if (name !== '') {
        localStorage.setItem('profileName', name);
        alert('Name saved successfully!');
    }
});

// --- Solution 2: Saving and Parsing JSON Arrays ---
const sampleTasks = ['Learn JS', 'Build an App', 'Deploy to Web'];

// Save array as JSON string
localStorage.setItem('tasks', JSON.stringify(sampleTasks));

// Retrieve and parse array back
const storedTasksString = localStorage.getItem('tasks');
const tasksArray = JSON.parse(storedTasksString);

console.log('Loaded Tasks:', tasksArray);