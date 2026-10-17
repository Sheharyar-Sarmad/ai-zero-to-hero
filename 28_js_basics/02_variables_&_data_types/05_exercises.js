// ============================================
// 05_exercises.js
// Solve each task below. Check answers in 06_solution.js
// Open DevTools Console (F12) to see the output.
// ============================================

// --- Part A: Predict the output (write your guess in a comment first) ---
// 1. console.log(a); var a = 10;
// 2. console.log(b); let b = 20;
// 3. console.log(typeof NaN);
// 4. console.log(typeof [1, 2, 3]);
// 5. console.log(typeof null);
// 6. let x = 10; const y = x; x = 20; console.log(y);
// 7. const obj = { name: "Ali" }; obj.name = "Ahmed"; console.log(obj.name);
// 8. console.log("5" + 3 * 2);

// --- Part B: Coding tasks ---

// Task 1: Variable Declarations
// Declare a variable `studentName` using `const` and assign your name.
// Declare a variable `score` using `let` and assign 95.
// Reassign `score` to 98 and print both.

// Task 2: Block Scope
// Use a block (`{}`) with `let` and `var` inside it.
// Try to log both variables outside the block. Notice which one throws an error.

// Task 3: Template Literals
// Given `const firstName = "Ayesha";` and `const age = 22;`,
// use a template literal to print: "Hello, my name is Ayesha and I am 22 years old."

// Task 4: Type Conversion
// Given `let strNum = "123.45";`, convert it into:
// - An integer using parseInt()
// - A floating-point number using parseFloat()
// - A number using Number()
// Print each result along with its `typeof`.

// Task 5: Primitive vs Reference
// Given `let score1 = 50; let score2 = score1; score2 = 80;`,
// print both score1 and score2. Explain why changing score2 didn't affect score1.

// Task 6: Object and Array Types
// Create an object representing a car (brand, model, year) 
// and an array of 3 favorite fruits. Print both and check their `typeof`.

// --- Part C: Challenge ---
// Write a snippet that checks if a variable `val` is strictly an Array 
// (since typeof array returns "object"). Test it with an array and a regular object.