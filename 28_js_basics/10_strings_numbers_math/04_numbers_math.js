// ============================================
// 04_numbers_math.js
// Examples of number formatting and Math object functions
// Open DevTools Console (F12) to see output.
// ============================================

console.log("=== 1. Number Formatting ===");
const price = 45.6789;
console.log("Fixed to 2 decimals:", price.toFixed(2)); // "45.68"
console.log("Is 42 an integer?", Number.isInteger(42));   // true

console.log("\n=== 2. Basic Math Functions ===");
console.log("Round 4.6:", Math.round(4.6)); // 5
console.log("Floor 4.9:", Math.floor(4.9)); // 4
console.log("Ceil 4.1:", Math.ceil(4.1));   // 5
console.log("Square root of 81:", Math.sqrt(81)); // 9
console.log("Power (2^3):", Math.pow(2, 3)); // 8

console.log("\n=== 3. Min, Max, and Random ===");
console.log("Max value:", Math.max(12, 45, 2, 88, 33)); // 88
console.log("Random (0 to 1):", Math.random());

// Generating a random integer between 1 and 10
const randomInt = Math.floor(Math.random() * 10) + 1;
console.log("Random int (1-10):", randomInt);