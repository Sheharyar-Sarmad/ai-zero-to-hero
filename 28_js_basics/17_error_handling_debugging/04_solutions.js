// ==========================================
// SOLUTIONS: Error Handling & Debugging
// ==========================================

// --- Solution 1: Try, Catch, and Throw ---
function divideNumbers(a, b) {
    if (b === 0) {
        throw new Error('Division by zero is not allowed.');
    }
    return a / b;
}

// Testing the error handler
try {
    console.log('Attempting division...');
    let result = divideNumbers(10, 0);
    console.log('Result:', result);
} catch (error) {
    console.error('Caught an error:', error.message);
} finally {
    console.log('Operation complete.');
}

// --- Solution 2: Basic Debugging Tools ---
const sampleData = [
    { id: 1, item: 'Apple', price: 1.2 },
    { id: 2, item: 'Banana', price: 0.8 }
];

// Neatly display data in the console
console.table(sampleData);