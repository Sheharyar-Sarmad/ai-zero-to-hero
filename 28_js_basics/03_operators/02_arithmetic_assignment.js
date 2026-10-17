// ============================================
// 02_arithmetic_assignment.js
// Practice for: Arithmetic & Assignment Operators
// Open DevTools Console (F12) to see the output.
// ============================================

console.log("=== Arithmetic Operators ===");

let a = 10;
let b = 3;

console.log("a + b =", a + b);   // 13
console.log("a - b =", a - b);   // 7
console.log("a * b =", a * b);   // 30
console.log("a / b =", a / b);   // 3.3333333333333335
console.log("a % b =", a % b);   // 1
console.log("a ** b =", a ** b); // 1000

// --- Remainder use cases ---
console.log("\n=== Remainder Use Cases ===");
let number = 7;
console.log(number + " is even?", number % 2 === 0); // false

let colors = ["red", "green", "blue"];
for (let i = 0; i < 7; i++) {
  console.log(i, "->", colors[i % colors.length]); // cycles through the array
}

// --- Increment / Decrement ---
console.log("\n=== Increment & Decrement ===");
let x = 5;
console.log("x++ returns:", x++); // 5
console.log("x is now:", x);      // 6
console.log("++x returns:", ++x); // 7
console.log("x-- returns:", x--); // 7
console.log("--x returns:", --x); // 5

// --- + with strings ---
console.log("\n=== + with Strings ===");
console.log(5 + 5);       // 10
console.log("5" + "5");   // "55"
console.log("5" + 5);     // "55"
console.log("5" - 2);     // 3
console.log("5" * "2");   // 10
console.log("Hello" - 2); // NaN

// --- Precedence ---
console.log("\n=== Precedence ===");
console.log(2 + 3 * 4);     // 14
console.log((2 + 3) * 4);   // 20
console.log(2 ** 3 ** 2);   // 512 (exponent goes right to left)

// --- Assignment operators ---
console.log("\n=== Assignment Operators ===");
let score = 10;
score += 5;  console.log("after += 5:", score);  // 15
score -= 3;  console.log("after -= 3:", score);  // 12
score *= 2;  console.log("after *= 2:", score);  // 24
score /= 4;  console.log("after /= 4:", score);  // 6
score %= 4;  console.log("after %= 4:", score);  // 2
score **= 3; console.log("after **= 3:", score); // 8

// --- Gotchas ---
console.log("\n=== Gotchas ===");
console.log("0.1 + 0.2 =", 0.1 + 0.2);                  // 0.30000000000000004
console.log("Fixed:", (0.1 + 0.2).toFixed(2));          // "0.30"
console.log("5 / 0 =", 5 / 0);                          // Infinity
console.log("-5 / 0 =", -5 / 0);                        // -Infinity
console.log("0 / 0 =", 0 / 0);                          // NaN