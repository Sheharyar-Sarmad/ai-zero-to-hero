// ============================================
// 05_exercises.js
// Solve each task below. Check answers in 06_solutions.js
// Open DevTools Console (F12) to see the output.
// ============================================

// --- Part A: Predict the output (write your guess in a comment first) ---
// 1. const obj = { a: 1, b: 2 }; const { a, c = 5 } = obj; console.log(a, c);
// 2. const user = { name: "Ali", greet() { return `Hi ${this.name}`; } }; console.log(user.greet());
// 3. const item = { price: 100 }; item.price = 200; console.log(item.price);
// 4. const obj1 = { x: 10 }; const obj2 = { ...obj1, y: 20 }; console.log(obj2.x);

// --- Part B: Coding tasks ---

// Task 1: Object Creation & Nested Access
// Create an object `car` with properties `brand`, `model`, and an object `specs` (horsepower, transmission).
// Print the car's horsepower using dot notation.

// Task 2: Object Methods
// Add a method `getDetails` to the `car` object from Task 1 
// that returns a string summarizing the brand and model (e.g., "2024 Toyota Corolla").

// Task 3: Iterating Over Objects
// Given an object `const scores = { math: 85, english: 90, science: 78 };`,
// use `Object.entries()` in a loop to print each subject and its score.

// Task 4: Destructuring with Renaming
// Given `const user = { id: 101, email: "sara@gmail.com" };`,
// destructure `email` into a variable named `userEmail`.

// Task 5: Merging Objects
// Given two objects `const profile = { name: "David", age: 30 };` and `const job = { role: "Developer", age: 32 };`,
// merge them using the spread operator. Notice how `age` is handled.

// --- Part C: Challenge ---
// Write a function `countProperties(obj)` that counts how many total properties 
// exist inside an object (without using external libraries).