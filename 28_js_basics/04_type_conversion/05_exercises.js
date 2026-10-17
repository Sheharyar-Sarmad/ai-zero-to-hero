// ============================================
// 05_exercises.js
// Solve each task below. Check answers in 06_solutions.js
// Open DevTools Console (F12) to see the output.
// ============================================

// --- Part A: Predict the output (write your guess in a comment first) ---
// 1. console.log("5" + 2 - 1);
// 2. console.log("10" * "3");
// 3. console.log(Boolean("false"));
// 4. console.log(Number(null) + Number(undefined));
// 5. console.log("5" == 5);
// 6. console.log(typeof (+"100"));
// 7. console.log(!"" + 5);
// 8. console.log(1 + 2 + "3");

// --- Part B: Coding tasks ---

// Task 1: Explicitly convert user inputs
// Given `let userInput = "45.7abc";`, use parseInt and parseFloat 
// to extract the numbers and log both results.

// Task 2: Strict checking vs loose checking
// Given `let num = 10; let str = "10";`, write an expression 
// checking equality using both `==` and `===`. Explain why results differ.

// Task 3: Falsy detection
// Given an array of mixed values: `[0, "hello", "", null, 42, undefined, false, "0"]`,
// write a loop or filter that extracts only truthy values.

// Task 4: Safe string calculation
// Given `let itemPrice = "150.50"; let tax = "12.25";`,
// explicitly convert them to numbers, add them up, and print the total nicely formatted.

// --- Part C: Challenge ---
// Without using built-in conversion functions like Number() or parseInt(),
// convert the string `"456"` into the number `456` using mathematical operators.