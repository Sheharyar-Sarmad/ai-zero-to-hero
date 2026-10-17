# Module 14: Timers and Asynchronous Intervals (Part 1 - `setTimeout`)

JavaScript is single-threaded, meaning it executes one line of code at a time. However, it uses asynchronous functions like timers to schedule tasks to run later without blocking the main execution thread.

## 1. The `setTimeout` Function
`setTimeout` is used to execute a specific block of code (a callback function) *once* after a specified delay in milliseconds.

```javascript
// Syntax: setTimeout(callbackFunction, delayInMilliseconds);

console.log('Start');

setTimeout(() => {
    console.log('This runs after 2 seconds (2000ms)');
}, 2000);

console.log('End');
// Output order: "Start" -> "End" -> "This runs after 2 seconds..."
```

## 2. Canceling a Timer with clearTimeout

When you call setTimeout, it returns a unique timer ID. If you need to cancel the scheduled execution before it runs, you can pass that ID to clearTimeout().

```javaScript
const timerId = setTimeout(() => {
    console.log('This will never run.');
}, 5000);

// Cancel the timer immediately
clearTimeout(timerId);
```