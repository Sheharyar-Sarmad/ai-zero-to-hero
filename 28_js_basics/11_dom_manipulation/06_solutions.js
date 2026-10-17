// ============================================
// 06_solutions.js
// Try the exercises first before looking here.
// Open DevTools Console (F12) to see the output.
// ============================================

console.log("=== Part A: Answers ===");
console.log("1. textContent reads/writes raw text safely. innerHTML parses and renders HTML tags inside strings.");
console.log("2. querySelectorAll returns a static NodeList (does not auto-update if DOM changes).");
console.log("3. classList.toggle() automatically checks presence: adds if missing, removes if present in one clean line.");

console.log("\n=== Part B: Solutions ===");

// Task 1
const actionBtn = document.getElementById("action-btn");
console.log("Button initial text:", actionBtn ? actionBtn.textContent : "Not found");

// Task 2
if (actionBtn) {
    actionBtn.style.backgroundColor = "black";
    actionBtn.style.color = "white";
    actionBtn.style.padding = "8px 16px";
    actionBtn.style.cursor = "pointer";
    actionBtn.textContent = "Processed!";
}

// Task 3
const appContainer = document.getElementById("app");
if (appContainer) {
    const techList = document.createElement("ul");
    const items = ["HTML", "CSS", "JavaScript"];
    
    items.forEach(tech => {
        const li = document.createElement("li");
        li.textContent = tech;
        techList.appendChild(li);
    });
    
    appContainer.appendChild(techList);
}

// Task 4
if (appContainer) {
    appContainer.setAttribute("data-status", "active");
    const statusVal = appContainer.getAttribute("data-status");
    console.log("Container data-status attribute:", statusVal); // "active"
}

console.log("\n=== Part C: Challenge ===");
const allParagraphs = document.querySelectorAll("p");
allParagraphs.forEach((p, index) => {
    // Avoid re-prepending if already added
    if (!p.textContent.startsWith("[")) {
        p.textContent = `[${index + 1}] ${p.textContent}`;
    }
});
console.log("Challenge completed: Number badges added to all paragraphs.");