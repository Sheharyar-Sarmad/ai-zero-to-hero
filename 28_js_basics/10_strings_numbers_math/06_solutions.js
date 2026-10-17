// ============================================
// 06_solutions.js
// Try the exercises first before looking here.
// Open DevTools Console (F12) to see the output.
// ============================================

console.log("=== Part A: Answers ===");
const sAns = "hello"; 
console.log("1.", sAns.charAt(1));                // "e"

console.log("2.", Math.floor(5.9));                 // 5

const numStrAns = "123.456"; 
console.log("3.", Number(Number(numStrAns).toFixed(2))); // 123.46

console.log("4.", "Frontend Developer".includes("end")); // true

console.log("\n=== Part B: Solutions ===");

// Task 1
const capitalizeFirst = str => str.charAt(0).toUpperCase() + str.slice(1).toLowerCase();
console.log("Capitalized:", capitalizeFirst("javascript")); // "Javascript"

// Task 2
const email = "developer_123@gmail.com";
const [username, domain] = email.split("@");
const maskedEmail = "*".repeat(username.length) + "@" + domain;
console.log("Masked Email:", maskedEmail); // "***********@gmail.com"

// Task 3
const generateRandomPassword = () => {
    const chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";
    let password = "";
    for (let i = 0; i < 6; i++) {
        const randomIndex = Math.floor(Math.random() * chars.length);
        password += chars[randomIndex];
    }
    return password;
};
console.log("Random Password:", generateRandomPassword());

// Task 4
const rawPrice = 1250.5;
const formattedCurrency = `$${rawPrice.toFixed(2)}`;
console.log("Formatted Price:", formattedCurrency); // "\$1250.50"

console.log("\n=== Part C: Challenge ===");
const countVowels = str => {
    const matches = str.match(/[aeiou]/gi);
    return matches ? matches.length : 0;
};
console.log("Vowel count in 'Programming':", countVowels("Programming")); // 3 (o, a, i)