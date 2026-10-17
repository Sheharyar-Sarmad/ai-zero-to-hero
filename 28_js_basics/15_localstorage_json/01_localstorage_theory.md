# Module 15: LocalStorage and JSON (Part 1 - LocalStorage Basics)

Web storage objects (`localStorage` and `sessionStorage`) allow JavaScript to save key-value pairs directly in a user's browser.

## 1. What is `localStorage`?
* **Persistence:** Data stored in `localStorage` has **no expiration time**. It persists even after the browser is closed, the tab is refreshed, or the computer is restarted (until explicitly cleared by code or user settings).
* **Scope:** It is tied to the origin (protocol + domain + port). Data stored by a website can only be accessed by that same website.
* **Storage Limit:** Typically allows around 5MB to 10MB of string data per domain.

## 2. Core `localStorage` Methods
1. **`localStorage.setItem(key, value)`**: Stores a key-value pair. Both the key and the value **must be strings**.
2. **`localStorage.getItem(key)`**: Retrieves the value associated with the given key. Returns `null` if the key does not exist.
3. **`localStorage.removeItem(key)`**: Deletes a specific key-value pair.
4. **`localStorage.clear()`**: Deletes *all* items stored in `localStorage` for that domain.

```javascript
// Saving data
localStorage.setItem('username', 'Alice');

// Retrieving data
const currentUser = localStorage.getItem('username');
console.log(currentUser); // "Alice"

// Removing data
localStorage.removeItem('username');
```