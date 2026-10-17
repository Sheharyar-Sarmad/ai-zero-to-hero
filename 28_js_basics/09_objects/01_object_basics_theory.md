# Object Basics in JavaScript

An **object** is a collection of related data and/or functionality, stored as a collection of **key-value pairs**. Each key is also known as a **property** (or a **method** if the value is a function).

## Creating Objects
The most common way to create an object is using **Object Literal** syntax (`{}`):
```javascript
const user = {
    firstName: "Alice",
    age: 25,
    isAdmin: true
};
```

## Accessing Object Properties

**Dot Notation**: The standard and most readable way.

```javaScript
console.log(user.firstName); // "Alice"
```

**Bracket Notation**: Useful when property names have spaces, special characters, or are stored in variables.

```javaScript
console.log(user["age"]); // 25
```

## Modifying & Adding Properties

Objects are mutable collections. You can update existing values, add new properties, or delete properties dynamically:

```javaScript
user.age = 26;          // Update existing
user.location = "NY";   // Add new property
delete user.isAdmin;    // Delete property
```