// ============================================
// 04_advanced_objects.js
// Examples of methods, this keyword, destructuring, and static object methods
// Open DevTools Console (F12) to see output.
// ============================================

console.log("=== 1. Methods and `this` Keyword ===");
const calculator = {
    numA: 10,
    numB: 5,
    add() {
        return this.numA + this.numB;
    }
};
console.log("Sum via method:", calculator.add());

console.log("\n=== 2. Object Static Methods ===");
const book = { title: "JavaScript Guide", author: "John Doe", year: 2024 };
console.log("Keys:", Object.keys(book));
console.log("Values:", Object.values(book));
console.log("Entries:", Object.entries(book));

console.log("\n=== 3. Object Destructuring ===");
const { title, year } = book;
console.log(`Title: ${title}, Year: ${year}`);

console.log("\n=== 4. Object Spreading & Merging ===");
const defaults = { theme: "dark", notifications: true };
const userPreferences = { notifications: false, sound: "chime" };
const finalSettings = { ...defaults, ...userPreferences }; 
console.log("Merged settings:", finalSettings); // userPreferences overrides defaults for 'notifications'