// =====================================================
// 04_data_types.js  –  JavaScript Data Types (simple)
// Run with:  node 04_data_types.js
// =====================================================

// -----------------------------------------------------
// 1. PRIMITIVE TYPES  (simple values, copied by value)
// -----------------------------------------------------
console.log("--- 1. Primitives ---");

let userName = "Ali";          // string  -> text
let age = 22;                  // number  -> whole number
let price = 9.99;              // number  -> decimals are also "number"
let isStudent = true;          // boolean -> true or false
let city;                      // undefined -> declared, no value yet
let emptyBox = null;           // null    -> empty on purpose
let bigNum = 12345678901234567890n; // bigint -> ends with n
let id = Symbol("id");         // symbol  -> always unique

// typeof tells us the type of a value
console.log(typeof userName);  // string
console.log(typeof age);       // number
console.log(typeof isStudent); // boolean
console.log(typeof city);      // undefined
console.log(typeof emptyBox);  // object  <- famous JS bug (it's really null)
console.log(typeof bigNum);    // bigint
console.log(typeof id);        // symbol

// -----------------------------------------------------
// 2. STRING  (text)
// -----------------------------------------------------
console.log("--- 2. String ---");

let text = "  Hello JavaScript  ";
console.log(text.length);              // 20  -> number of characters (with spaces)
console.log(text.trim());              // "Hello JavaScript" -> removes extra spaces
console.log(text.toUpperCase());       // "  HELLO JAVASCRIPT  "
console.log(text.toLowerCase());       // "  hello javascript  "
console.log(text.includes("Java"));    // true  -> is this word inside?
console.log(text.trim().slice(0, 5));  // "Hello" -> cut from index 0 to 5
console.log(text.trim().split(" "));   // [ 'Hello', 'JavaScript' ] -> string to array
console.log(text.replace("Hello", "Hi")); // replace a word

// Template literal: use backticks ` ` and ${ } to put values inside text
console.log(`My name is ${userName} and I am ${age} years old.`);

// -----------------------------------------------------
// 3. NUMBER
// -----------------------------------------------------
console.log("--- 3. Number ---");

console.log(10 + 5);    // 15
console.log(10 % 3);    // 1   -> remainder
console.log(2 ** 3);    // 8   -> power (2 x 2 x 2)
console.log(0.1 + 0.2); // 0.30000000000000004 -> decimal precision issue
console.log(1 / 0);     // Infinity
console.log("abc" * 2); // NaN -> Not a Number

// Math helpers
console.log(Math.round(4.6));  // 5  -> nearest whole number
console.log(Math.floor(4.9));  // 4  -> round down
console.log(Math.ceil(4.1));   // 5  -> round up
console.log(Math.max(1, 5, 3));// 5  -> biggest
console.log(Math.random());    // random number between 0 and 1

// -----------------------------------------------------
// 4. BOOLEAN – TRUTHY & FALSY
// -----------------------------------------------------
console.log("--- 4. Truthy / Falsy ---");

// These 8 values are FALSY (act like false):
// false, 0, -0, 0n, "", null, undefined, NaN
console.log(Boolean(0));        // false
console.log(Boolean(""));       // false
console.log(Boolean(null));     // false
// Everything else is TRUTHY:
console.log(Boolean("hello"));  // true
console.log(Boolean([]));       // true  (empty array is truthy!)
console.log(Boolean("0"));      // true  (it's a non-empty string)

// -----------------------------------------------------
// 5. UNDEFINED vs NULL
// -----------------------------------------------------
console.log("--- 5. undefined vs null ---");

let a1;                         // JS gives it undefined automatically
let b1 = null;                  // we set null ourselves
console.log(a1);                // undefined
console.log(b1);                // null
console.log(null == undefined); // true  -> loosely equal
console.log(null === undefined);// false -> different types

// -----------------------------------------------------
// 6. PRIMITIVE vs REFERENCE  (very important!)
// -----------------------------------------------------
console.log("--- 6. Value vs Reference ---");

// Primitive: a real COPY is made
let x = 5;
let y = x;          // y gets its own copy of 5
y = 10;             // changing y does NOT touch x
console.log(x, y);  // 5 10

// Object: both names point to the SAME object
let obj1 = { score: 1 };
let obj2 = obj1;    // no copy, same object
obj2.score = 99;    // changing obj2 changes obj1 too
console.log(obj1.score); // 99

// To make a real copy, use spread { ...obj }
let obj3 = { ...obj1 };
obj3.score = 0;
console.log(obj1.score); // 99 -> unchanged, because obj3 is a copy

// -----------------------------------------------------
// 7. OBJECT  { key: value }
// -----------------------------------------------------
console.log("--- 7. Object ---");

const student = {
  name: "Sara",
  age: 20,
  skills: ["HTML", "CSS"],
};

console.log(student.name);       // Sara    -> dot notation
console.log(student["age"]);     // 20      -> bracket notation

student.city = "Lahore";         // add a new property
student.age = 21;                // update a property
delete student.skills;           // remove a property
console.log(student);            // { name: 'Sara', age: 21, city: 'Lahore' }

console.log(Object.keys(student));   // [ 'name', 'age', 'city' ]
console.log(Object.values(student)); // [ 'Sara', 21, 'Lahore' ]

// Destructuring: take values out into variables
const { name, city: studentCity } = student;
console.log(name, studentCity);      // Sara Lahore

// -----------------------------------------------------
// 8. ARRAY  [ ordered list ]
// -----------------------------------------------------
console.log("--- 8. Array ---");

const fruits = ["apple", "banana", "mango"];

console.log(fruits[0]);          // apple -> index starts at 0
console.log(fruits.length);      // 3

fruits.push("orange");           // add to the END
fruits.unshift("kiwi");          // add to the START
fruits.pop();                    // remove from the END
fruits.shift();                  // remove from the START
console.log(fruits);             // [ 'apple', 'banana', 'mango' ]

console.log(fruits.includes("banana")); // true
console.log(fruits.indexOf("mango"));   // 2
console.log(fruits.join(", "));         // "apple, banana, mango"

// The 3 most useful array methods:
const nums = [1, 2, 3, 4, 5];
console.log(nums.map((n) => n * 2));         // [2,4,6,8,10] -> change every item
console.log(nums.filter((n) => n % 2 === 0));// [2,4]        -> keep matching items
console.log(nums.reduce((sum, n) => sum + n, 0)); // 15      -> combine into one value

// -----------------------------------------------------
// 9. FUNCTION  (also a value)
// -----------------------------------------------------
console.log("--- 9. Function ---");

function add(a, b) {             // normal function
  return a + b;
}
const multiply = (a, b) => a * b; // arrow function (shorter)

console.log(add(2, 3));          // 5
console.log(multiply(2, 3));     // 6
console.log(typeof add);         // function

// -----------------------------------------------------
// 10. TYPE CONVERSION
// -----------------------------------------------------
console.log("--- 10. Type Conversion ---");

// Explicit: we convert on purpose
console.log(Number("42"));       // 42
console.log(Number("abc"));      // NaN
console.log(String(123));        // "123"
console.log(parseInt("42px"));   // 42
console.log(parseFloat("3.14")); // 3.14

// Implicit: JS converts automatically (can surprise you!)
console.log("5" + 2);            // "52" -> + joins text
console.log("5" - 2);            // 3    -> - converts to numbers
console.log(true + 1);           // 2    -> true becomes 1

// -----------------------------------------------------
// 11. == vs ===
// -----------------------------------------------------
console.log("--- 11. == vs === ---");

console.log("5" == 5);           // true  -> == ignores type
console.log("5" === 5);          // false -> === checks type too
console.log(0 == false);         // true  (confusing!)
console.log(0 === false);        // false (clear) -> ALWAYS use ===

// -----------------------------------------------------
// 12. CHECKING TYPES CORRECTLY
// -----------------------------------------------------
console.log("--- 12. Type Checking ---");

console.log(typeof []);              // object  <- not helpful
console.log(Array.isArray([]));      // true    -> the right way for arrays
console.log(Number.isNaN(NaN));      // true    -> the right way for NaN
console.log(typeof null === "object" && null === null); // check null with === null

// -----------------------------------------------------
// 13. const DOES NOT FREEZE OBJECTS
// -----------------------------------------------------
console.log("--- 13. const ---");

const list = [1, 2];
list.push(3);                    // allowed -> we change the inside
console.log(list);               // [ 1, 2, 3 ]
// list = [];                    // ERROR -> can't re-assign a const

console.log("\nDone!");