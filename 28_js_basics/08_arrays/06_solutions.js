// ============================================
// 06_solutions.js
// Try the exercises first before looking here.
// Open DevTools Console (F12) to see the output.
// ============================================

console.log("=== Part A: Answers ===");
const arrAns = [10, 20, 30]; arrAns.splice(1, 1, 99); 
console.log("1.", arrAns);                        // [10, 99, 30]

const wordsAns = ["js", "python", "go"]; 
console.log("2.", wordsAns.map(w => w.toUpperCase())); // ["JS", "PYTHON", "GO"]

const numsAns = [5, 10, 15]; 
console.log("3.", numsAns.reduce((acc, n) => acc + n, 5)); // 35 (5 + 5 + 10 + 15)

const itemsAns = [1, 2, 2, 3, 4, 4]; 
console.log("4.", [...new Set(itemsAns)].length); // 4 (unique elements count)

console.log("\n=== Part B: Solutions ===");

// Task 1
let tech = ["HTML", "CSS"];
tech.push("JavaScript");
tech.unshift("Git");
console.log("Updated tech array:", tech);

// Task 2
const numbers = [3, 14, 7, 22, 9, 18];
const greaterThanTen = numbers.filter(n => n > 10);
console.log("Numbers > 10:", greaterThanTen); // [14, 22, 18]

// Task 3
const users = [
    {firstName: "John", lastName: "Doe"}, 
    {firstName: "Sara", lastName: "Ali"}
];
const fullNames = users.map(u => `${u.firstName} ${u.lastName}`);
console.log("Full names:", fullNames); // ["John Doe", "Sara Ali"]

// Task 4
const pricesList = [15.50, 42.00, 8.99, 100.00];
const totalCost = pricesList.reduce((acc, price) => acc + price, 0);
console.log("Total Cost: \$", totalCost.toFixed(2)); // \$166.49

// Task 5
const inventory = [{id: 101, item: "Pen"}, {id: 102, item: "Notebook"}];
const foundItem = inventory.find(i => i.id === 102);
console.log("Found item:", foundItem); // {id: 102, item: "Notebook"}

console.log("\n=== Part C: Challenge ===");
const chunkArray = (arr, size) => {
    const chunked = [];
    for (let i = 0; i < arr.length; i += size) {
        chunked.push(arr.slice(i, i + size));
    }
    return chunked;
};
console.log("Chunked array:", chunkArray([1, 2, 3, 4, 5], 2)); // [[1, 2], [3, 4], [5]]