// ============================================
// 02_object_basics.js
// Examples of object creation, property access, and mutation
// Open DevTools Console (F12) to see output.
// ============================================

console.log("=== 1. Creating and Accessing Objects ===");
const student = {
    name: "Sara",
    "student id": 1042,
    major: "Computer Science",
    isEnrolled: true
};

console.log("Name (Dot notation):", student.name);
console.log("ID (Bracket notation):", student["student id"]); // Required for keys with spaces

console.log("\n=== 2. Modifying and Adding Properties ===");
student.major = "Software Engineering"; // Update
student.gpa = 3.8;                     // Add new property
console.log("Updated student object:", student);

console.log("\n=== 3. Nested Objects ===");
const userProfile = {
    username: "coder123",
    address: {
        city: "Lahore",
        country: "Pakistan"
    }
};
console.log("City:", userProfile.address.city);