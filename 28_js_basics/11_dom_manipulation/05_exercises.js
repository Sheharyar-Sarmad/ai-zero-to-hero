// ============================================
// 05_exercises.js
// Solve each task below. Check answers in 06_solutions.js
// Open DevTools Console (F12) to see the output.
// ============================================

// --- Part A: Predict the output / conceptual questions (write guess in comments) ---
// 1. What is the difference between `textContent` and `innerHTML`?
// 2. Does `querySelectorAll` return a live HTMLCollection or a static NodeList?
// 3. Why is `classList.toggle()` preferred over manual conditional checks for adding/removing classes?

// --- Part B: DOM Coding Tasks (Test inside index.html) ---

// Task 1: Select by ID
// Select the button element with id `"action-btn"` using `document.getElementById` 
// and log its text content to the console.

// Task 2: Change Button Text and Background
// Using the button selected in Task 1, change its background color to `"black"` 
// and its text color to `"white"`, and update its text to `"Processed!"`.

// Task 3: Create a List Dynamically
// Create an unordered list (`<ul>`) containing 3 list items (`<li>` with items "HTML", "CSS", "JavaScript") 
// using JavaScript loops and append it inside the `#app` container.

// Task 4: Attribute Manipulation
// Select the `#app` container, set a custom attribute data-status="active" on it, 
// and then read that attribute back using `getAttribute`.

// --- Part C: Challenge ---
// Write a script that finds all paragraphs (`<p>`) inside the document, 
// and appends a sequential number badge at the beginning of each (e.g., "[1] This is a paragraph").