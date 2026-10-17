// ============================================
// 04_break_continue.js
// Examples of break and continue statements
// Open DevTools Console (F12) to see output.
// ============================================

console.log("=== 1. Using Break ===");
for (let i = 1; i <= 5; i++) {
    if (i === 4) {
        console.log("Found 4, breaking out of loop!");
        break;
    }
    console.log(i);
}

console.log("\n=== 2. Using Continue ===");
for (let i = 1; i <= 5; i++) {
    if (i === 3) {
        console.log("Skipping 3!");
        continue;
    }
    console.log(i);
}