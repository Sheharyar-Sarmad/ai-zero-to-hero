# Module 14: Timers and Asynchronous Intervals (Part 2 - `setInterval`)

While `setTimeout` runs a function once after a delay, `setInterval` repeatedly executes a function at fixed time intervals.

## 1. The `setInterval` Function
`setInterval` continuously runs the callback function until it is explicitly stopped.

```javascript
// Syntax: setInterval(callbackFunction, intervalInMilliseconds);

let count = 0;

const intervalId = setInterval(() => {
    count++;
    console.log(`Interval count: ${count}`);
    
    // Stop after 5 ticks
    if (count === 5) {
        clearInterval(intervalId);
        console.log('Interval stopped.');
    }
}, 1000); // Runs every 1 second
```

## 2. Important Gotchas with Timers

- **Timing Precision**: Timers in JavaScript are not 100% precise. Because JavaScript is single-threaded, if the main execution stack is busy running heavy computations, a timer's callback may be delayed.

- **Memory Leaks**: Always clear your intervals using clearInterval() when leaving a page component or when a condition is met, otherwise the process will run indefinitely in the background.