# Module 15: LocalStorage and JSON (Part 2 - JSON Objects & Arrays)

`localStorage` can **only store strings**. If you try to save a JavaScript object or array directly, it will be automatically converted to the string `"[object Object]"`, destroying its structure. 

To store complex data structures, we use **JSON (JavaScript Object Notation)**.

## 1. Converting Data with JSON
1. **`JSON.stringify(value)`**: Converts a JavaScript object or array into a JSON-formatted string so it can be saved in `localStorage`.
2. **`JSON.parse(text)`**: Takes a JSON string retrieved from `localStorage` and converts it back into a usable JavaScript object or array.

```javascript
// Storing an array/object
const userPreferences = { theme: 'dark', notifications: true };

// Convert object to string and save
localStorage.setItem('prefs', JSON.stringify(userPreferences));

// Retrieve string and convert back to object
const savedPrefsString = localStorage.getItem('prefs');
const parsedPrefs = JSON.parse(savedPrefsString);

console.log(parsedPrefs.theme); // "dark"