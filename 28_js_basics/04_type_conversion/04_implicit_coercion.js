// ============================================
// 04_implicit_coercion.js
// Examples of automatic (implicit) type coercion
// Open DevTools Console (F12) to see output.
// ============================================

console.log("=== 1. String Concatenation vs Arithmetic ===");
console.log("5" + 3);   // "53" (Number 3 coerced to string)
console.log("5" - 3);   // 2 (String "5" coerced to number)
console.log("10" * "2");// 20 (Both strings coerced to numbers)
console.log("10" / 2);  // 5

console.log("\n=== 2. Quirky Coercion Examples ===");
console.log("5" + true);  // "5true"
console.log(5 + true);    // 6 (true coerced to 1)
console.log("5" - true);  // 4 (true coerced to 1, string to number)
console.log([] + {});     // "[object Object]"
console.log([1] + [2]);   // "12"