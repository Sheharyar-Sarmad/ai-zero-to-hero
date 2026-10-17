# Module 13: Forms and Input Validation (Part 2 - Validation Logic)

Once you capture input values, you validate them using conditional statements and regular expressions (RegEx) or built-in HTML5 properties.

## 1. Common Validation Checks
1. **Empty Field Checks:** Checking if a string is empty or contains only whitespace (`value.trim() === ''`).
2. **Length Constraints:** Ensuring passwords or usernames meet minimum/maximum length requirements (`value.length < 8`).
3. **Pattern Matching (Regex):** Verifying specific formats like emails, phone numbers, or postal codes using regular expressions (`pattern.test(value)`).

## 2. Providing Feedback to Users
When validation fails, you should:
*   Prevent the form from processing further.
*   Display clear error messages near the respective input fields or inside an error container.
*   Add visual cues (such as adding a CSS error class like `.error` or changing border colors to red).

## 3. Client-Side vs Server-Side Validation
*   **Client-Side (JavaScript / HTML5):** Fast, immediate feedback for the user. Improves UX.
*   **Server-Side (Backend):** Mandatory for true security. Never trust client-side validation alone, as users can bypass or disable JavaScript in their browsers.