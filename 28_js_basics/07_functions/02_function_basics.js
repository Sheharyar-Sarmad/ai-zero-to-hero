// ============================================
// 02_function_basics.js
// Examples of function declarations, expressions, and parameters
// Open DevTools Console (F12) to see output.
// ============================================

console.log("=== 1. Function Declaration & Invocation ===");
function sayHello(name = "Guest") {
    return `Welcome back, ${name}!`;
}
console.log(sayHello("Sara"));
console.log(sayHello()); // Uses default parameter

console.log("\n=== 2. Function Expression ===");
const calculateSquare = function(num) {
    return num * num;
};
console.log("Square of 4:", calculateSquare(4));

console.log("\n=== 3. Function with Multiple Arguments ===");
function sumAll(a, b, c) {
    return a + b + c;
}
console.log("Sum:", sumAll(10, 20, 30));