// ============================================
// 05_exercises.js
// Solve each task below. Check answers in 06_solutions.js
// Open DevTools Console (F12) to see the output.
// ============================================

// --- Part A: Predict the output (write your guess in a comment first) ---
// 1. console.log(10 % 4);
// 2. console.log("10" + 5);
// 3. console.log("10" - 5);
// 4. console.log(2 + 3 * 2 ** 2);
// 5. console.log(5 == "5", 5 === "5");
// 6. console.log(0 || "A", 0 ?? "A");
// 7. console.log(true && "yes");
// 8. console.log(typeof null);

// --- Part B: Coding tasks ---

// Task 1: Given `let num = 17;`
// Print whether it is even or odd using % and a ternary.

// Task 2: Given price = 250 and quantity = 4,
// calculate the total, then apply a 10% discount using *= .
// Print the final amount.

// Task 3: Given `let counter = 5;`
// Use ++ and -- so the console prints 5, 7, 7, 5 in that order.
// (Hint: mix prefix and postfix.)

// Task 4: Given username = "" and defaultName = "Guest",
// print the name to display using ||, then using ??.
// Explain in a comment why the results differ.

// Task 5: Given age = 25 and hasLicense = true,
// print whether the person can drive (age >= 18 AND has license).

// Task 6: Given `let marks = 83;`
// Use a ternary chain to print the grade:
// 90+ = A, 80+ = B, 70+ = C, otherwise F.

// Task 7: Given temperature = 35,
// print "Hot" if above 30, "Cold" if below 15, otherwise "Pleasant".

// Task 8: Given const student = { name: "Sara", scores: { math: 90 } };
// Safely print student.scores.english using optional chaining,
// and print "Not available" if it is undefined (use ??).

// --- Part C: Challenge ---
// Fix the floating point problem: make 0.1 + 0.2 print exactly 0.3
// (as a number, not a string).