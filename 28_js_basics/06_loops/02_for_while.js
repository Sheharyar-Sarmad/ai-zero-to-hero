// ============================================
// 02_for_while.js
// Examples of for, while, and do...while loops
// Open DevTools Console (F12) to see output.
// ============================================

console.log("=== 1. Standard For Loop ===");
for (let i = 1; i <= 3; i++) {
    console.log(`For loop count: ${i}`);
}

console.log("\n=== 2. While Loop ===");
let count = 1;
while (count <= 3) {
    console.log(`While loop count: ${count}`);
    count++;
}

console.log("\n=== 3. Do...While Loop ===");
let num = 1;
do {
    console.log(`Do-while num: ${num}`);
    num++;
} while (num <= 3);