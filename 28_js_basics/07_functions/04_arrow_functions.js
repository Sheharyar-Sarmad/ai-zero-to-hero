// ============================================
// 04_arrow_functions.js
// Examples of arrow functions and implicit returns
// Open DevTools Console (F12) to see output.
// ============================================

console.log("=== 1. Standard Arrow Function ===");
const greetUser = (name) => {
    return `Hello, ${name} from an arrow function!`;
};
console.log(greetUser("Ahmed"));

console.log("\n=== 2. Concise Arrow Function (Implicit Return) ===");
const cube = n => n * n * n;
console.log("Cube of 3:", cube(3));

console.log("\n=== 3. Multiple Parameters Arrow Function ===");
const addNumbers = (a, b) => a + b;
console.log("Sum: 15 + 25 =", addNumbers(15, 25));