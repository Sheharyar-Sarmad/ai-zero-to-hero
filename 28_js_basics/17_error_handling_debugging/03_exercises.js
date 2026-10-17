// ==========================================
// EXERCISES: Error Handling & Debugging
// ==========================================

// Instructions:
// 1. Write a function called `divideNumbers(a, b)` that takes two numbers.
// 2. Inside the function, use an `if` statement to check if `b` is equal to 0.
//    If it is, `throw` a new Error with the message: "Division by zero is not allowed."
// 3. Otherwise, return `a / b`.
// 4. Wrap a call to `divideNumbers(10, 0)` inside a `try...catch` block 
//    so that the application doesn't crash, and log the caught error message to the console.