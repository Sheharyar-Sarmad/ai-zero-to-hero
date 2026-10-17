// ============================================
// 06_solutions.js
// Try the exercises first before looking here.
// Open DevTools Console (F12) to see the output.
// ============================================

console.log("=== Part A: Answers ===");
console.log(10 % 4);                // 2
console.log("10" + 5);              // "105"
console.log("10" - 5);              // 5
console.log(2 + 3 * 2 ** 2);        // 14  (2 ** 2 = 4, 3 * 4 = 12, 2 + 12)
console.log(5 == "5", 5 === "5");   // true false
console.log(0 || "A", 0 ?? "A");    // "A" 0
console.log(true && "yes");         // "yes"
console.log(typeof null);           // "object"

console.log("\n=== Part B: Solutions ===");

// Task 1
let num = 17;
console.log(num + " is", num % 2 === 0 ? "even" : "odd"); // odd

// Task 2
let price = 250;
let quantity = 4;
let total = price * quantity; // 1000
total *= 0.9;                 // 10% discount
console.log("Final amount:", total); // 900

// Task 3
// Goal: print 5, 7, 7, 5
let c = 5;
console.log(c);       // 5
c++;                  // 6
console.log(++c);     // 7
console.log(c--);     // 7 (returns old value, then c becomes 6)
console.log(--c);     // 5

// Task 4
const username = "";
const defaultName = "Guest";
console.log(username || defaultName); // "Guest"
console.log(username ?? defaultName); // ""
// || treats "" as falsy and uses the default.
// ?? only falls back for null/undefined, so "" is kept.

// Task 5
const age = 25;
const hasLicense = true;
console.log("Can drive:", age >= 18 && hasLicense); // true

// Task 6
let marks = 83;
const grade = marks >= 90 ? "A" : marks >= 80 ? "B" : marks >= 70 ? "C" : "F";
console.log("Grade:", grade); // B

// Task 7
const temperature = 35;
const feel = temperature > 30 ? "Hot" : temperature < 15 ? "Cold" : "Pleasant";
console.log(feel); // Hot

// Task 8
const student = { name: "Sara", scores: { math: 90 } };
console.log(student.scores?.english ?? "Not available"); // "Not available"

console.log("\n=== Part C: Challenge ===");
console.log(Number((0.1 + 0.2).toFixed(2))); // 0.3
// Alternative: work in whole units
console.log((0.1 * 10 + 0.2 * 10) / 10);     // 0.3