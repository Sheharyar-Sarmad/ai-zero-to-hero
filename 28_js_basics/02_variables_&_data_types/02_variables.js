
console.log("VARIABLES IN JAVASCRIPT");

// 1. What is a variable?
let name = "Ali";
let age = 25;

console.log("\n1. Variables:");
console.log("Name:", name);
console.log("Age:", age);


// 2. Three ways to create variables

// let - value can change
let score = 0;
score = 10;
console.log("\n2. let:", score);

// const - cannot be reassigned
const PI = 3.14159;
console.log("const PI:", PI);

// var - old way of declaring variables
var color = "red";
var color = "blue"; // Redeclaration is allowed
console.log("var color:", color);


// 3. Block scope: let, const, and var
if (true) {
    let a = 1;
    const b = 2;
    var c = 3;

    console.log("\n3. Inside block:");
    console.log("let a:", a);
    console.log("const b:", b);
    console.log("var c:", c);
}

// console.log(a); // ReferenceError: block-scoped
// console.log(b); // ReferenceError: block-scoped
console.log("var outside block:", c);


// 4. Choosing between let and const
const siteName = "MyShop";
let totalPrice = 1000;

totalPrice += 500;

console.log("\n4. Use cases:");
console.log("Site:", siteName);
console.log("Total price:", totalPrice);


// 5. Variable naming
let firstName = "Ali";
let lastName = "Khan";
const MAX_SPEED = 120;
let isLoggedIn = true;

console.log("\n5. Naming:");
console.log("First name:", firstName);
console.log("Last name:", lastName);
console.log("Max speed:", MAX_SPEED);
console.log("Logged in:", isLoggedIn);

// Invalid examples:
// let 1name = "Ali";  // Cannot start with a number
// let first-name = "Ali"; // Hyphens are not allowed
// let let = 10; // Reserved keyword


// 6.1 Declaration, assignment, and initialization
let x; // Declaration
x = 5; // Assignment
let y = 10; // Initialization

console.log("\n6.1 Declaration and assignment:");
console.log("x:", x);
console.log("y:", y);


// 6.2 Reassigning a variable
let level = 1;
level = 2;
level = 3;

console.log("\n6.2 Reassignment:", level);


// 6.3 Copying a variable
let a = 10;
let b = a;

a = 20;

console.log("\n6.3 Copying:");
console.log("a:", a);
console.log("b:", b);


// 6.4 Mathematical operations
let apples = 5;

apples = apples + 2;
apples += 3;
apples -= 1;
apples *= 2;
apples /= 3;

console.log("\n6.4 Math operations:", apples);


// 6.5 Increment and decrement
let count = 0;

count++;
count++;
count--;

console.log("\n6.5 Increment and decrement:", count);


// 6.6 Joining strings
let first = "Ali";
let last = "Khan";

let fullName = first + " " + last;

console.log("\n6.6 String concatenation:", fullName);
console.log(`Hello, my name is ${fullName}.`);


// 6.7 Swapping two variables
let num1 = 1;
let num2 = 2;

[num1, num2] = [num2, num1];

console.log("\n6.7 Swapping:", num1, num2);


// 6.8 Declaring multiple variables
let p = 1, q = 2, r = 3;

console.log("\n6.8 Multiple variables:", p, q, r);


// 6.9 Variables can hold different data types
let data = 42;
console.log("\n6.9 Data types:");
console.log(data, typeof data);

data = "hello";
console.log(data, typeof data);

data = true;
console.log(data, typeof data);


// 6.10 Displaying a variable
let city = "Lahore";

console.log("\n6.10 Displaying values:");
console.log("City:", city);

// Uncomment to show a browser popup:
// alert(city);


// 7. Common mistakes
console.log("\n7. Common mistakes:");

// const fixedValue = 10;
// fixedValue = 20; // TypeError: Assignment to constant variable

// let username = "Ali";
// let username = "Ahmed"; // SyntaxError: already declared

// Always declare variables with let or const.
// Avoid accidental global variables.


// 8. Practice exercises
console.log("\nPRACTICE");

// Exercise 1: Create and print your name
let myName = "Sheharyar";
console.log("My name:", myName);

// Exercise 2: Calculate age from birth year
const birthYear = 2000;
const currentYear = new Date().getFullYear();
let myAge = currentYear - birthYear;

console.log("Birth year:", birthYear);
console.log("Age:", myAge);

// Exercise 3: Increase score by 10 three times
let practiceScore = 0;

practiceScore += 10;
practiceScore += 10;
practiceScore += 10;

console.log("Practice score:", practiceScore);

// Exercise 4: Try changing a const
// Uncomment the next two lines to see the error:
// const country = "Pakistan";
// country = "England";

console.log("\nEND OF VARIABLES LESSON");
