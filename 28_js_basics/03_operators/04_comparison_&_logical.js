// ============================================
// 04_comparison_logical.js
// Practice for: Comparison, Logical & Other Operators
// Open DevTools Console (F12) to see the output.
// ============================================

console.log("=== Comparison Operators ===");
console.log(5 == "5");   // true  (loose)
console.log(5 === "5");  // false (strict)
console.log(5 != "5");   // false
console.log(5 !== "5");  // true
console.log(7 > 3, 7 < 3, 7 >= 7, 3 <= 2); // true false true false

console.log("\n=== Special Cases ===");
console.log(NaN === NaN);              // false
console.log(Number.isNaN(NaN));        // true
console.log(null == undefined);        // true
console.log(null === undefined);       // false
console.log([] == false);              // true (confusing, so avoid ==)
console.log("b" > "a");                // true
console.log("apple" < "banana");       // true
console.log([1] === [1]);              // false (different references)

console.log("\n=== Logical Operators ===");
const hasTicket = true;
const isAdult = false;
console.log("AND:", hasTicket && isAdult); // false
console.log("OR:", hasTicket || isAdult);  // true
console.log("NOT:", !hasTicket);           // false

console.log("\n=== Short-Circuit Evaluation ===");
console.log("hello" && "world"); // "world"
console.log("" && "world");      // ""
console.log("" || "default");    // "default"
console.log("value" || "default"); // "value"

const userName = "";
console.log("Welcome,", userName || "Guest"); // Welcome, Guest

const isLoggedIn = true;
isLoggedIn && console.log("Showing dashboard..."); // runs only if true

console.log("\n=== Nullish Coalescing (??) ===");
console.log(0 || 10);        // 10
console.log(0 ?? 10);        // 0
console.log("" ?? "empty");  // ""
console.log(null ?? "fallback");      // "fallback"
console.log(undefined ?? "fallback"); // "fallback"

console.log("\n=== Ternary Operator ===");
const age = 20;
console.log(age >= 18 ? "Adult" : "Minor"); // Adult

const marks = 72;
const grade = marks >= 90 ? "A" : marks >= 70 ? "B" : "C"; // nested (use sparingly)
console.log("Grade:", grade); // B

console.log("\n=== typeof ===");
console.log(typeof 42);          // "number"
console.log(typeof "hi");        // "string"
console.log(typeof true);        // "boolean"
console.log(typeof undefined);   // "undefined"
console.log(typeof null);        // "object" (famous JS bug)
console.log(typeof [1, 2]);      // "object"
console.log(typeof function () {}); // "function"

console.log("\n=== Optional Chaining (?.) ===");
const user = { name: "Ali", address: { city: "Lahore" } };
console.log(user.address?.city);   // "Lahore"
console.log(user.contact?.phone);  // undefined (no error)

console.log("\n=== Spread (...) ===");
const arr1 = [1, 2];
const arr2 = [3, 4];
console.log([...arr1, ...arr2]); // [1, 2, 3, 4]

console.log("\n=== in & instanceof ===");
console.log("name" in user);          // true
console.log("age" in user);           // false
console.log([] instanceof Array);     // true