# Function Basics in JavaScript

Functions are reusable blocks of code designed to perform a particular task. They allow you to write modular and maintainable code.

## 1. Function Declaration

Declared using the `function` keyword. Function declarations are **hoisted**, meaning they can be called before they are defined in the code.

```javascript
function greet(name) {
    return `Hello, ${name}!`;
}
```

## 2. Function Expression

Created by storing an anonymous or named function inside a variable. They are **not hoisted**.

```javascript
const add = function(a, b) {
    return a + b;
};
```

## 3. Parameters and Arguments

- **Parameters:** Variables listed inside the function definition parentheses.
- **Arguments:** Real values passed to the function when it is invoked.
- **Default Parameters:** Fallback values assigned to parameters if no argument is passed.

```javascript
function multiply(a, b = 1) {
    return a * b;
}

multiply(5);    // 5
multiply(5, 3); // 15
```