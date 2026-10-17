// ============================================
// 06_solution.js
// Try the exercises first before looking here.
// Open DevTools Console (F12) to see the output.
// ============================================

console.log("=== Part A: Answers ===");
console.log("1.", undefined);                     // var is hoisted with undefined
// console.log("2.", ReferenceError);            // let is hoisted in Temporal Dead Zone
console.log("3.", typeof NaN);                    // "number"
console.log("4.", typeof [1, 2, 3]);              // "object"
console.log("5.", typeof null);                   // "object" (historical JS bug)
let x = 10; const y = x; x = 20; 
console.log("6.", y);                             // 10 (primitive value copied)
const obj = { name: "Ali" }; obj.name = "Ahmed"; 
console.log("7.", obj.name);                      // "Ahmed" (const blocks reassignment, not mutation)
console.log("8.", "5" + 3 * 2);                   // "56" (operator precedence: 3*2 = 6, then concatenation)

console.log("\n=== Part B: Solutions ===");

// Task 1
const studentName = "Ali";
let score = 95;
score = 98;
console.log("Student:", studentName, "| Score:", score);

// Task 2
{
    let blockLet = "I am block scoped";
    var functionVar = "I am function/global scoped";
}
// console.log(blockLet); // ReferenceError: blockLet is not defined outside block
console.log(functionVar); // "I am function/global scoped" (var leaks out)

// Task 3
const firstName = "Ayesha";
const age = 22;
console.log(`Hello, my name is ${firstName} and I am ${age} years old.`);

// Task 4
let strNum = "123.45";
console.log(parseInt(strNum), typeof parseInt(strNum));         // 123 "number"
console.log(parseFloat(strNum), typeof parseFloat(strNum));     // 123.45 "number"
console.log(Number(strNum), typeof Number(strNum));             // 123.45 "number"

// Task 5
let score1 = 50;
let score2 = score1;
score2 = 80;
console.log("score1:", score1, "score2:", score2); // 50, 80
// Explanation: Primitives are copied by value, creating independent memory spaces.

// Task 6
const car = { brand: "Toyota", model: "Corolla", year: 2022 };
const fruits = ["Apple", "Banana", "Mango"];
console.log("Car:", car, "| Type:", typeof car);
console.log("Fruits:", fruits, "| Type:", typeof fruits);

console.log("\n=== Part C: Challenge ===");
const testArray = [1, 2, 3];
const testObj = { a: 1 };
console.log("Is testArray an array?", Array.isArray(testArray)); // true
console.log("Is testObj an array?", Array.isArray(testObj));       // false