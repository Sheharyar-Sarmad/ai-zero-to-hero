# Module 16: Fetch API (Part 2 - Async/Await)

While `.then()` chains work well, modern JavaScript favors **`async/await`** syntax because it makes asynchronous code look and behave more like synchronous code, making it much easier to read and debug.

## 1. Using `async` and `await`
To use `await`, you must wrap your code inside a function declared with the `async` keyword. You can then "pause" execution until the Promise resolves.

```javascript
async function fetchData() {
    try {
        const response = await fetch('[https://jsonplaceholder.typicode.com/todos/1](https://jsonplaceholder.typicode.com/todos/1)');
        
        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }
        
        const data = await response.json();
        console.log('Fetched Data:', data);
    } catch (error) {
        console.error('Failed to fetch data:', error);
    }
}

fetchData();
```

## 2. Why use try...catch?

Network requests can fail for many reasons (bad URLs, offline status, server downtime). Wrapping await calls in a try...catch block ensures that any errors thrown during the fetch or parsing process are cleanly caught and handled.