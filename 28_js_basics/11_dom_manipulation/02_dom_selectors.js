// ============================================
// 02_dom_selectors.js
// Examples of selecting HTML elements using various DOM methods
// Open DevTools Console (F12) to see output.
// ============================================

console.log("=== 1. Selecting by ID ===");
const appContainer = document.getElementById("app");
console.log("App Container:", appContainer);

console.log("\n=== 2. Selecting using querySelector ===");
const mainTitle = document.querySelector(".title");
console.log("Main Title Element:", mainTitle);

console.log("\n=== 3. Selecting using querySelectorAll ===");
const allParagraphs = document.querySelectorAll("p");
console.log("Total paragraphs found:", allParagraphs.length);
allParagraphs.forEach((p, index) => {
    console.log(`Paragraph ${index}:`, p.textContent);
});

console.log("\n=== 4. Selecting by Class Name ===");
const descriptiveElements = document.getElementsByClassName("description");
console.log("Elements with class 'description':", descriptiveElements);