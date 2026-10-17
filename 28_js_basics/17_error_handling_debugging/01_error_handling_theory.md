# Module 17: Error Handling & Debugging (Part 1 - Try/Catch/Throw)

Even experienced developers write code that produces errors. Error handling allows your application to catch unexpected issues gracefully instead of completely crashing.

## 1. Types of Errors in JavaScript
* **Syntax Errors:** Mistakes in grammar/punctuation (e.g., missing a closing parenthesis `)`). The script won't run at all.
* **Runtime Errors (Exceptions):** Errors that occur while the code is running (e.g., trying to call a method on an undefined variable).
* **Logical Errors:** The code runs without crashing, but produces the wrong result due to a mistake in the algorithm.

## 2. The `try...catch` Statement
You wrap risky code inside a `try` block. If an error occurs, JavaScript immediately stops executing the `try` block and jumps into the `catch` block, passing along an error object.

```javascript
try {
    // Code that might fail
    let result = unknownVariable.someMethod();
} catch (error) {
    // Code to handle the error gracefully
    console.log('An error occurred:', error.message);
} finally {
    // Optional: Runs regardless of whether an error occurred or not
    console.log('Execution finished.');
}
```

## 3. Creating Custom Errors with throw

You can manually generate your own errors using the throw keyword when certain business conditions fail (e.g., checking if a user entered a negative age).

```javaScript
function validateAge(age) {
    if (age < 0) {
        throw new Error('Age cannot be negative!');
    }
    return 'Valid age';
}
```