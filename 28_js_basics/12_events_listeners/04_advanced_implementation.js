// ==========================================
// 3. REMOVING EVENT LISTENERS
// ==========================================

const submitBtn = document.querySelector('#submitBtn');

function handleSubmission(event) {
    console.log('Form submitted! Removing listener to prevent double submission.');
    
    // Must pass the exact same function reference
    submitBtn.removeEventListener('click', handleSubmission);
}

submitBtn.addEventListener('click', handleSubmission);