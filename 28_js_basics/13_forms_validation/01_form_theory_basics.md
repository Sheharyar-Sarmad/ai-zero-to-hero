# Module 13: Forms and Input Validation (Part 1 - Basics)

Form validation ensures that users provide correct and properly formatted data before a web form is submitted to a server. 

## 1. Why Validate Forms?
*   **Data Integrity:** Ensures the data received matches expected formats (e.g., valid email address, secure password).
*   **User Experience (UX):** Provides immediate feedback so users can fix mistakes before submission.
*   **Security:** Prevents malformed or malicious inputs from reaching the backend server.

## 2. Preventing Default Form Submission
By default, submitting an HTML `<form>` causes the browser to refresh the page. In JavaScript, we intercept the `submit` event and use `event.preventDefault()` to stop the reload and validate data asynchronously via script.

```javascript
const form = document.querySelector('#signupForm');

form.addEventListener('submit', (event) => {
    // Stop the page from reloading
    event.preventDefault();
    console.log('Form submission intercepted for validation.');
});
```

## 3. Accessing Form Input Values

You can access input values directly using the .value property on the input DOM element.

- ```inputElement.value```: Returns the string currently typed into the input field.

- ```.trim()```: A string method used to remove leading and trailing whitespace (essential for checking if a field is actually empty).