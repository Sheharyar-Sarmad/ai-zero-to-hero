// ============================================
// 04_advanced_methods.js
// Examples of map, filter, reduce, and professional chaining
// Open DevTools Console (F12) to see output.
// ============================================

console.log("=== 1. map() Transformation ===");
const nums = [1, 2, 3, 4];
const doubled = nums.map(n => n * 2);
console.log("Doubled:", doubled); // [2, 4, 6, 8]

console.log("\n=== 2. filter() Selection ===");
const scores = [45, 88, 92, 30, 75];
const passing = scores.filter(s => s >= 70);
console.log("Passing scores:", passing); // [88, 92, 75]

console.log("\n=== 3. reduce() Accumulation ===");
const prices = [10, 20, 30, 40];
const total = prices.reduce((acc, curr) => acc + curr, 0);
console.log("Total sum:", total); // 100

console.log("\n=== 4. Professional Method Chaining ===");
const cart = [
    { name: "Laptop", price: 1200, inStock: true },
    { name: "Mouse", price: 30, inStock: true },
    { name: "Keyboard", price: 80, inStock: false }
];
const affordableInStockTotal = cart
    .filter(item => item.inStock && item.price < 100)
    .map(item => item.price)
    .reduce((sum, price) => sum + price, 0);

console.log("Affordable in-stock total:", affordableInStockTotal); // 30