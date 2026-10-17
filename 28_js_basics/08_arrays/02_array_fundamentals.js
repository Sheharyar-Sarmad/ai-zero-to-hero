// ============================================
// 02_array_fundamentals.js
// Examples of array basics, indexing, and core operations
// Open DevTools Console (F12) to see output.
// ============================================

console.log("=== 1. Creation and Accessing Elements ==p");
const fruits = ["apple", "banana", "mango"];
console.log("First item:", fruits[0]); // apple
console.log("Last item:", fruits[fruits.length - 1]); // mango

console.log("\n=== 2. Mutating Methods (push, pop, unshift, shift) ===");
let tasks = ["Code", "Eat"];
tasks.push("Sleep");     // Adds to end
tasks.unshift("Wake up");// Adds to start
console.log("After adding:", tasks);

tasks.pop();             // Removes from end
tasks.shift();           // Removes from start
console.log("After removing:", tasks);

console.log("\n=== 3. Non-Mutating Methods (slice, includes, join) ===");
const numbers = [10, 20, 30, 40, 50];
console.log("Slice (1 to 4):", numbers.slice(1, 4)); // [20, 30, 40]
console.log("Includes 30?", numbers.includes(30));     // true
console.log("Joined string:", numbers.join(" - "));    // 10 - 20 - 30 - 40 - 50