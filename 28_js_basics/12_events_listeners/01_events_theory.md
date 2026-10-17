# Event Listeners Theory

Event listeners are methods in JavaScript that allow you to wait for and respond to user interactions or browser events (such as clicks, keypresses, and form submissions) on DOM elements.

## Key Concepts:
1. **`addEventListener()`**: The standard, most flexible way to register an event handler. It allows you to attach multiple listeners to a single element without overwriting existing ones.
2. **The Event Object (`event`)**: Automatically passed to the callback function, containing metadata about the event (e.g., target element, key pressed, mouse coordinates).
3. **`removeEventListener()`**: Used to clean up listeners. Requires a direct reference to the handler function (anonymous functions cannot be removed).