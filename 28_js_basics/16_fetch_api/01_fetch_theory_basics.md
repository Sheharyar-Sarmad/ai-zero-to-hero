# Module 16: Fetch API (Part 1 - Making Requests & Promises)

Modern JavaScript uses the built-in **Fetch API** to make HTTP requests (GET, POST, etc.) to servers and retrieve data asynchronously.

## 1. What is Fetch?
The `fetch()` method starts the process of fetching a resource from a network. It returns a **Promise** that resolves to the `Response` object representing the response to the request.

```javascript
// Basic GET request structure
fetch('[https://api.example.com/data](https://api.example.com/data)')
    .then(response => {
        // Handle response
    })
    .catch(error => {
        // Handle network errors
    });
```

## 2. Handling Response Streams (Response.json())

When you receive a response from fetch(), it isn't the raw data yet—it's a representation of the HTTP response. To convert the response body into a usable JavaScript object or array, you must call .json(), which also returns a Promise.

