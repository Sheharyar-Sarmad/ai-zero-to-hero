// ============================================
// 06_solutions.js
// Try the exercises first before looking here.
// Open DevTools Console (F12) to see the output.
// ============================================

console.log("=== Part A: Answers ===");
console.log("1.", "5" + 2 - 1);         // 51 ("5" + 2 becomes "52", then "52" - 1 becomes 51)
console.log("2.", "10" * "3");          // 30 (strings coerced to numbers)
console.log("3.", Boolean("false"));    // true (non-empty string is truthy)
console.log("4.", Number(null) + Number(undefined)); // NaN (0 + NaN = NaN)
console.log("5.", "5" == 5);            // true (loose equality performs type coercion)
console.log("6.", typeof (+"100"));     // "number" (unary plus operator converts string to number)
console.log("7.", !"" + 5);             // 6 (!"" is true, true coerced to 1, 1 + 5 = 6)
console.log("8.", 1 + 2 + "3");         // "33" (1+2=3, then 3 + "3" = "33")

console.log("\n=== Part B: Solutions ===");

// Task 1
let userInput = "45.7abc";
console.log("parseInt:", parseInt(userInput));     // 45
console.log("parseFloat:", parseFloat(userInput)); // 45.7

// Task 2
let num = 10;
let str = "10";
console.log("Loose (==):", num == str);   // true (coerces string to number)
console.log("Strict (===):", num === str); // false (different types: number vs string)

// Task 3
const mixedValues = [0, "hello", "", null, 42, undefined, false, "0"];
const truthyValues = mixedValues.filter(Boolean);
console.log("Truthy values:", truthyValues); // ["hello", 42, "0"]

// Task 4
let itemPrice = "150.50";
let tax = "12.25";
let totalAmount = Number(itemPrice) + Number(tax);
console.log(`Total Price: $${totalAmount.toFixed(2)}`); // Total Price: \$162.75

console.log("\n=== Part C: Challenge ===");
let strNum = "456";
let convertedNum = strNum * 1; // or Number(strNum), but using math coercion: strNum - 0
console.log(convertedNum, typeof convertedNum); // 456 "number"