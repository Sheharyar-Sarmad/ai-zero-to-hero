// ============================================
// 02_strings.js
// Examples of string properties and manipulation methods
// Open DevTools Console (F12) to see output.
// ============================================

console.log("=== 1. Length and Indexing ===");
const text = "  JavaScript Developer  ";
console.log("Length:", text.length);
console.log("Character at index 4:", text[4]);

console.log("\n=== 2. Case and Whitespace Management ===");
const cleanText = text.trim();
console.log("Trimmed:", `"${cleanText}"`);
console.log("Uppercase:", cleanText.toUpperCase());
console.log("Lowercase:", cleanText.toLowerCase());

console.log("\n=== 3. Searching and Extracting ===");
const sentence = "Learning JavaScript is fun and rewarding.";
console.log("Includes 'fun'?", sentence.includes("fun"));
console.log("Index of 'Script':", sentence.indexOf("Script"));
console.log("Slice (9, 19):", sentence.slice(9, 19)); // "JavaScript"

console.log("\n=== 4. Replacing and Splitting ===");
const updatedSentence = sentence.replace("fun", "awesome");
console.log("Replaced:", updatedSentence);
const wordsArray = cleanText.split(" ");
console.log("Split into array:", wordsArray);