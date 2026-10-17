# Comprehensive Theory: Modifying the DOM

Once you have selected an element from the DOM tree, you can read or modify its content, attributes, and styles using built-in properties and methods.

---

## 1. Content Modification Properties
- **`element.textContent`**: Gets or sets the raw text content inside an element (ignores HTML tags, safe from XSS attacks).
- **`element.innerHTML`**: Gets or sets the HTML markup inside an element (parses strings as actual HTML tags).

## 2. Attribute & Property Management
- **`element.getAttribute("attr")`** / **`element.setAttribute("attr", "value")`**: Read or write custom/standard HTML attributes (like `src`, `href`, `alt`).
- **`element.id` / `element.className`**: Directly access or change standard properties.

## 3. Styling & Class Manipulation
- **`element.style.property = "value"`**: Applies inline CSS styles directly (e.g., `element.style.backgroundColor = "red"`).
- **`element.classList.add("className")`**
- **`element.classList.remove("className")`**
- **`element.classList.toggle("className")`**: Adds the class if missing, removes it if present (best practice for dynamic states like dark mode or UI toggles).

## 4. Creating and Inserting New Elements
- **`document.createElement("tagName")`**: Generates a brand-new element in memory.
- **`parent.appendChild(element)`**: Appends the new element as the last child.
- **`parent.remove()`**: Deletes an element from the DOM entirely.