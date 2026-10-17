// ============================================
// 06_solutions.js
// Try the exercises first before looking here.
// Open DevTools Console (F12) to see the output.
// ============================================

console.log("=== Part A: Answers ===");
const multiplyAns = (a, b) => a * b; 
console.log("1.", multiplyAns(4, 5));             // 20

function testAns(x = 10, y = 20) { return x + y; } 
console.log("2.", testAns(5));                    // 25 (x=5, y uses default 20)

const sayHiAns = name => `Hi ${name}`; 
console.log("3.", sayHiAns("Ali"));               // "Hi Ali"

console.log("\n=== Part B: Solutions ===");

// Task 1
function isEven(num) {
    return num % 2 === 0;
}
console.log("Is 4 even?", isEven(4));   // true
console.log("Is 7 even?", isEven(7));   // false

// Task 2
const findMax = function(a, b) {
    return a > b ? a : b;
};
console.log("Max between 12 and 19:", findMax(12, 19)); // 19

// Task 3
const calculateArea = (width, height) => width * height;
console.log("Area (5x10):", calculateArea(5, 10)); // 50

// Task 4
const convertToCelsius = f => (f - 32) * 5 / 9;
console.log("68°F in Celsius:", convertToCelsius(68)); // 20

// Task 5
const processArray = (arr, fn) => {
    let result = [];
    for (let i = 0; i < arr.length; i++) {
        result.push(fn(arr[i]));
    }
    return result;
};
const numbers = [1, 2, 3, 4];
console.log("Doubled numbers:", processArray(numbers, n => n * 2)); // [2, 4, 6, 8]

console.log("\n=== Part C: Challenge ===");
const factorial = n => {
    if (n === 0 || n === 1) return 1;
    return n * factorial(n - 1);
};
console.log("Factorial of 5:", factorial(5)); // 120