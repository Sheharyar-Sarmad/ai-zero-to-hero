# Module 17: Error Handling & Debugging (Part 2 - Basic Debugging)

Debugging is the art of tracking down *why* your code isn't working the way you expect. 

## 1. Using `console` Tools Effectively
Beyond basic `console.log()`, JavaScript provides specialized console methods to help organize debugging:
* `console.error(msg)`: Prints messages in red, marking them as errors.
* `console.warn(msg)`: Prints messages in yellow as warnings.
* `console.table(arrayOrObject)`: Displays arrays or objects neatly in a table format.

```javascript
const user = { name: 'Alice', role: 'Admin' };
console.table(user);
```

## 2. Using the Browser DevTools Debugger

- Console Tab: Where error logs and custom outputs appear.

- **Debugger Statement**: You can insert the keyword debugger; directly into your JavaScript code. When your browser's Developer Tools are open, JavaScript will automatically pause execution at that exact line, allowing you to inspect variables step-by-step.

```javaScript
function calculateTotal(price, tax) {
    debugger; // Browser will pause execution here if DevTools is open
    return price + (price * tax);
}
```