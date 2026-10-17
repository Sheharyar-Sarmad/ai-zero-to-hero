// ============================================
// 04_dom_modification.js
// Examples of modifying text, styles, classes, and creating new elements
// Open DevTools Console (F12) to see output.
// ============================================

// 1. Modifying Text Content
const titleElement = document.querySelector(".title");
if (titleElement) {
    titleElement.textContent = "Updated Title via JavaScript!";
}

// 2. Changing Inline Styles
const descriptionElement = document.querySelector(".description");
if (descriptionElement) {
    descriptionElement.style.color = "#0066cc";
    descriptionElement.style.fontWeight = "bold";
}

// 3. ClassList Manipulation
const appBox = document.getElementById("app");
if (appBox) {
    appBox.classList.add("highlight-box");
    console.log("Has 'highlight-box' class?", appBox.classList.contains("highlight-box"));
}

// 4. Creating and Appending a New Element Dynamically
const newParagraph = document.createElement("p");
newParagraph.textContent = "This paragraph was dynamically created and inserted via JS!";
newParagraph.style.color = "green";
appBox.appendChild(newParagraph);