// ==========================================
// SOLUTIONS: Fetch API
// ==========================================

const fetchBtn = document.querySelector('#fetchBtn');
const resultDiv = document.querySelector('#resultDiv');

async function fetchRandomUser() {
    try {
        resultDiv.textContent = 'Loading...';
        
        // Fetch data from public API endpoint
        const response = await fetch('https://jsonplaceholder.typicode.com/users/1');
        
        if (!response.ok) {
            throw new Error(`Server returned status: ${response.status}`);
        }
        
        const user = await response.json();
        
        // Display data on the DOM
        resultDiv.innerHTML = `
            <h3>User Found:</h3>
            <p><strong>Name:</strong> ${user.name}</p>
            <p><strong>Email:</strong> ${user.email}</p>
            <p><strong>City:</strong> ${user.address.city}</p>
        `;
    } catch (error) {
        console.error('Error fetching user:', error);
        resultDiv.textContent = 'Failed to load user data. Please try again.';
        resultDiv.style.color = 'red';
    }
}

fetchBtn.addEventListener('click', fetchRandomUser);