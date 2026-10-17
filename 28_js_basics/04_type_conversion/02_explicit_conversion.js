// ============================================
// 02_explicit_conversion.js
// Examples of manual (explicit) type conversion
// Open DevTools Console (F12) to see output.
// ============================================

console.log("=== 1. Converting to Number ===");
console.log(Number("123"));      // 123
console.log(Number("12.34"));    // 12.34
console.log(Number("hello"));    // NaN (Not a Number)
console.log(Number(true));       // 1
console.log(Number(false));      // 0
console.log(Number(null));       // 0
console.log(Number(undefined));  // NaN

console.log("\n=== 2. Using parseInt & parseFloat ===");
console.log(parseInt("100px"));   // 100
console.log(parseFloat("12.99 USD")); // 12.99

console.log("\n=== 3. Converting to String ===");
console.log(String(456));        // "456"
console.log(String(true));       // "true"
console.log((100).toString());   // "100"

console.log("\n=== 4. Converting to Boolean ===");
console.log(Boolean(1));         // true
console.log(Boolean(0));         // false
console.log(Boolean("hello"));   // true
console.log(Boolean(""));        // false (empty string)
console.log(Boolean(null));      // false
console.log(Boolean(undefined)); // false