# Variables in JavaScript

## 1. What is a Variable?

A **variable** is a **named box** that stores a value.

You give the box a name, put something inside it, and use it whenever you need it.

```
 ┌──────────┐
 │    25    │   ← value (what is stored)
 └──────────┘
     age        ← name (label on the box)
```

```js
let name = "Ali";
let age = 25;

console.log(name); // Ali
console.log(age);  // 25
```

**Why do we need variables?**

- To **store** information (a name, a score, a price)
- To **reuse** it without retyping
- To **change** it later when needed

---

## 2. Three Ways to Create a Variable

JavaScript gives us three keywords: **`let`**, **`const`** and **`var`**.

### `let` — for values that can change

```js
let score = 0;
score = 10;       // allowed, we changed the value
console.log(score); // 10
```

You **cannot** create the same `let` variable twice:

```js
let city = "Lahore";
// let city = "Karachi";  // Error: 'city' has already been declared
```

### `const` — for values that never change

`const` means **constant**. Once you put a value in, you cannot replace it.

```js
const PI = 3.14159;
// PI = 3;  // Error: Assignment to constant variable
```

A `const` **must** be given a value when it is created:

```js
// const country;   // Error: Missing initializer
const country = "Pakistan"; // correct
```

### `var` — the old way

`var` was the only option before 2015 (ES6). It still works, but it has confusing behaviors, so modern code avoids it.

```js
var color = "red";
var color = "blue";   // allowed (no error, easy to make mistakes)
color = "green";      // allowed
```

---

## 3. Differences at a Glance

| Feature                    | `let`            | `const`          | `var`                 |
| -------------------------- | ---------------- | ---------------- | --------------------- |
| Change the value           | Yes              | No               | Yes                   |
| Declare the same name twice | No               | No               | Yes (risky)           |
| Must have value at start   | No               | Yes              | No                    |
| Stays inside `{ }` block   | Yes              | Yes              | No (leaks out)        |
| Recommended today          | Yes              | Yes (first choice) | No                  |

### Block behavior (simple view)

A **block** is anything between `{ }`, like an `if` statement.

```js
if (true) {
  let a = 1;
  var b = 2;
}

// console.log(a); // Error: a only exists inside the block
console.log(b);    // 2  (var escapes the block, which can cause bugs)
```

---

## 4. Which One Should I Use? (Use Cases)

**Rule of thumb: start with `const`. Switch to `let` only if the value must change. Don't use `var`.**

| Situation                                   | Use     | Example                          |
| ------------------------------------------- | ------- | -------------------------------- |
| Value never changes                         | `const` | `const PI = 3.14;`               |
| Fixed settings, links, names                | `const` | `const siteName = "MyShop";`     |
| Counter, score, total that updates          | `let`   | `let score = 0;`                 |
| User input that changes over time           | `let`   | `let password = "";`             |
| Reading old code / legacy projects          | `var`   | (just recognize it)              |

> **Tip:** `const` with objects and arrays: you cannot replace the whole thing, but you can change what's inside.
>
> ```js
> const fruits = ["apple", "banana"];
> fruits.push("mango");   // allowed
> // fruits = [];         // Error
> ```

---

## 5. Naming Rules

**Rules (must follow):**

- Use letters, digits, `_` and `$`
- Cannot start with a number
- No spaces or dashes
- Cannot use reserved words (`let`, `const`, `class`, ...)
- Names are **case-sensitive** (`age` and `Age` are different)

**Good habits:**

- Use **camelCase**: `firstName`, `totalPrice`
- Use clear names: `userAge`, not `x`
- Constants can use UPPERCASE: `MAX_SPEED`
- Booleans often start with `is` or `has`: `isLoggedIn`

```js
let firstName = "Ali";   // good
// let 1name = "x";      // invalid, starts with a number
// let first-name = "x"; // invalid, has a dash
```

---

## 6. Fundamentals of Variable Manipulation

### 6.1 Declare, assign, initialize

```js
let x;        // declare (box is empty, value is undefined)
x = 5;        // assign (put a value in)
let y = 10;   // declare + initialize in one line
```

### 6.2 Reassigning (changing) a value

```js
let level = 1;
level = 2;
level = 3;
console.log(level); // 3
```

### 6.3 Copying one variable into another

```js
let a = 10;
let b = a;   // b gets a copy of the value
a = 20;

console.log(a); // 20
console.log(b); // 10  (b is not affected)
```

### 6.4 Using math on variables

```js
let apples = 5;

apples = apples + 2;  // 7
apples += 3;          // 10  (shortcut for apples = apples + 3)
apples -= 1;          // 9
apples *= 2;          // 18
apples /= 3;          // 6
```

### 6.5 Increment and decrement

```js
let count = 0;
count++;   // 1  (add 1)
count++;   // 2
count--;   // 1  (subtract 1)
```

### 6.6 Joining text (strings)

```js
let firstName = "Ali";
let lastName = "Khan";

let fullName = firstName + " " + lastName;
console.log(fullName); // Ali Khan

// Easier way: template literals (use backticks `)
console.log(`My name is ${fullName}`); // My name is Ali Khan
```

### 6.7 Swapping two variables

```js
let a = 1;
let b = 2;

[a, b] = [b, a];

console.log(a, b); // 2 1
```

### 6.8 Declaring many variables at once

```js
let x = 1, y = 2, z = 3;
```

### 6.9 Variables can hold different types

JavaScript lets a variable hold any kind of value, and even change type later.

```js
let data = 42;       // number
data = "hello";      // now a string
data = true;         // now a boolean
```

Check the type with `typeof`:

```js
console.log(typeof 42);       // "number"
console.log(typeof "hello");  // "string"
console.log(typeof true);     // "boolean"
```

### 6.10 Showing a variable's value

```js
let city = "Lahore";
console.log(city);        // shows in the browser console
alert(city);              // shows a popup
```

---

## 7. Common Mistakes

| Mistake                           | Problem                                 | Fix                                   |
| --------------------------------- | --------------------------------------- | ------------------------------------- |
| Changing a `const`                | Error                                   | Use `let` if the value must change    |
| Declaring same `let` twice        | Error                                   | Declare once, then just assign        |
| Using a variable before creating it | Error or `undefined`                  | Create it first, then use it          |
| Typos (`scroe` vs `score`)        | New/undefined variable                  | Check spelling carefully              |
| Forgetting `let`/`const`          | Creates a hidden global variable        | Always use `let` or `const`           |

---

## 8. Summary

- A variable is a **named container** for a value.
- **`const`**: value cannot be reassigned. Use it by default.
- **`let`**: value can change. Use it when you need updates.
- **`var`**: old style. Avoid it, but recognize it in old code.
- You can **assign, reassign, copy, calculate with, and combine** variables.
- Use clear **camelCase** names.

## Practice

1. Create a variable `myName` and print it.
2. Create `const birthYear = 2000` and calculate your age using another variable.
3. Make a `let score = 0`, increase it by 10 three times, and print it.
4. Try changing a `const` and read the error message.