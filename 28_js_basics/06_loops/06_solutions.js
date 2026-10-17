// ============================================
// 06_solutions.js
// Try the exercises first before looking here.
// Open DevTools Console (F12) to see the output.
// ============================================

console.log("=== Part A: Answers ===");
let sumAns = 0; for(let i = 1; i <= 3; i++) sumAns += i; 
console.log("1.", sumAns);                      // 6 (1 + 2 + 3)

console.log("2.");
for(let i = 0; i < 3; i++) { if(i === 1) continue; console.log(i); } // 0, then 2 (1 is skipped)

console.log("3.");
let x = 5; while(x > 0) { console.log(x); x -= 2; } // 5, 3, 1

console.log("\n=== Part B: Solutions ===");

// Task 1
console.log("Even numbers from 1 to 20:");
for (let i = 1; i <= 20; i++) {
    if (i % 2 === 0) console.log(i);
}

// Task 2
let totalSum = 0;
let j = 1;
while (j <= 100) {
    totalSum += j;
    j++;
}
console.log("Sum 1 to 100:", totalSum); // 5050

// Task 3
const base = 5;
console.log("Multiplication table of 5:");
for (let i = 1; i <= 10; i++) {
    console.log(`${base} x ${i} = ${base * i}`);
}

// Task 4
const colors = ["red", "green", "blue", "yellow"];
console.log("Uppercase colors:");
for (let i = 0; i < colors.length; i++) {
    console.log(colors[i].toUpperCase());
}

// Task 5
console.log("First number divisible by both 3 and 7:");
for (let i = 1; i <= 50; i++) {
    if (i % 3 === 0 && i % 7 === 0) {
        console.log(i);
        break;
    }
}

console.log("\n=== Part C: Challenge ===");
let pattern = "";
for (let i = 1; i <= 5; i++) {
    pattern += "*";
    console.log(pattern);
}