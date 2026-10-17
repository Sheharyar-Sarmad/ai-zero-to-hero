// ============================================
// 05_exercises.js
// Solve each task below. Check answers in 06_solutions.js
// Open DevTools Console (F12) to see the output.
// ============================================

// --- Part A: Predict the output (write your guess in a comment first) ---
// 1. const arr = [10, 20, 30]; arr.splice(1, 1, 99); console.log(arr);
// 2. const words = ["js", "python", "go"]; console.log(words.map(w => w.toUpperCase()));
// 3. const nums = [5, 10, 15]; console.log(nums.reduce((acc, n) => acc + n, 5));
// 4. const items = [1, 2, 2, 3, 4, 4]; console.log([...new Set(items)].length);

// --- Part B: Coding tasks ---

// Task 1: Basic Manipulation
// Given an array `let tech = ["HTML", "CSS"];`, add "JavaScript" to the end 
// and "Git" to the beginning using proper array methods.

// Task 2: Filtering Data
// Given an array `const numbers = [3, 14, 7, 22, 9, 18];`,
// use `filter` to get numbers greater than 10.

// Task 3: Transforming Objects
// Given an array of users `const users = [{firstName: "John", lastName: "Doe"}, {firstName: "Sara", lastName: "Ali"}];`,
// use `map` to return an array of full name strings ("John Doe", "Sara Ali").

// Task 4: Aggregate with Reduce
// Given an array of product prices `[15.50, 42.00, 8.99, 100.00]`,
// use `reduce` to calculate the total cost.

// Task 5: Advanced Search
// Given an array `const inventory = [{id: 101, item: "Pen"}, {id: 102, item: "Notebook"}];`,
// use `find` to extract the object where id is 102.

// --- Part C: Challenge ---
// Write a function `chunkArray(arr, size)` that splits an array into smaller chunks of a specified size 
// (e.g., chunkArray([1, 2, 3, 4, 5], 2) should return [[1, 2], [3, 4], [5]]).