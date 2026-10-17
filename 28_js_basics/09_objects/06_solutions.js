// ============================================
// 06_solutions.js
// Try the exercises first before looking here.
// Open DevTools Console (F12) to see the output.
// ============================================

console.log("=== Part A: Answers ===");
const objAns = { a: 1, b: 2 }; const { a, c = 5 } = objAns; 
console.log("1.", a, c);                          // 1 5 (c takes default value 5)

const userAns = { name: "Ali", greet() { return `Hi ${this.name}`; } }; 
console.log("2.", userAns.greet());               // "Hi Ali"

const itemAns = { price: 100 }; itemAns.price = 200; 
console.log("3.", itemAns.price);                 // 200 (properties of const objects can be modified)

const obj1Ans = { x: 10 }; const obj2Ans = { ...obj1Ans, y: 20 }; 
console.log("4.", obj2Ans.x);                     // 10 (spread copies properties)

console.log("\n=== Part B: Solutions ===");

// Task 1 & 2
const car = {
    brand: "Toyota",
    model: "Corolla",
    year: 2024,
    specs: {
        horsepower: 169,
        transmission: "Automatic"
    },
    getDetails() {
        return `${this.year} ${this.brand} ${this.model}`;
    }
};
console.log("Car Horsepower:", car.specs.horsepower); // 169
console.log("Car Details:", car.getDetails());          // "2024 Toyota Corolla"

// Task 3
const scores = { math: 85, english: 90, science: 78 };
console.log("Scores breakdown:");
for (const [subject, score] of Object.entries(scores)) {
    console.log(`${subject}: ${score}`);
}

// Task 4
const user = { id: 101, email: "sara@gmail.com" };
const { email: userEmail } = user;
console.log("User Email:", userEmail); // "sara@gmail.com"

// Task 5
const profile = { name: "David", age: 30 };
const job = { role: "Developer", age: 32 };
const mergedProfile = { ...profile, ...job };
console.log("Merged Profile:", mergedProfile); // { name: "David", age: 32, role: "Developer" }
// Explanation: Properties from later objects overwrite earlier ones (age becomes 32).

console.log("\n=== Part C: Challenge ===");
const countProperties = obj => Object.keys(obj).length;
const testObj = { name: "Ahmed", role: "Admin", active: true };
console.log("Total properties:", countProperties(testObj)); // 





